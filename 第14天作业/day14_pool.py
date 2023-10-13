import pandas as pd
import concurrent.futures
from collections import Counter
import os
import re
import timeit

# files too big, if you want to run the program, replace the following path to your location
path = "E:/Program_files/Tencent/QQdocument/day14asset/download"
filesloc = path + "/Texts"


def get_cnt(filepaths):
    # filepath = "E:/Program_files/Tencent/QQdocument/day14asset/download/Texts/aca/ACJ.xml"
    print("to process:")
    for filepath in filepaths:
        print("....", filepath)
    cnt = Counter([])
    for filepath in filepaths:
        with open(filepath, encoding="UTF-8") as file:
            content = file.read()
            content = re.sub(r"\W", " ", content)
            cnt += Counter(content.split())
    return cnt


def batch_file(filespath):
    names = os.listdir(filespath)
    size = 5
    threadCnt = Counter()
    if len(names) > 50: size = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        threads = []
        for i in range(0, len(names), size):
            countFile = executor.submit(get_cnt, [filespath + f"/{singlefile}" for singlefile in names[i:i + size]])
            threads.append(countFile)
    threadCnt += sum([thread.result() for thread in threads], Counter())
    return threadCnt


# testpath = "E:/Program_files/Tencent/QQdocument/day14asset/download/Texts/aca"
# batch_file(testpath)


def main():
    processCnt = Counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        names = os.listdir(filesloc)
        processes = []
        t = 0
        for dirs in names:
            if os.path.isdir(filesloc + f"/{dirs}"):
                processDir = executor.submit(batch_file, filesloc + f"/{dirs}")
                processes.append(processDir)
            t += 1
        processCnt += sum([process.result() for process in processes], Counter())
    res = pd.DataFrame(list(processCnt.items()), columns=["word", "count"])
    res.to_csv("./output.csv", index=None)


if __name__ == "__main__":
    cnttime = timeit.Timer("main()", "from __main__ import main")
    print("\n\n\nFinished in:", cnttime.timeit(number=1), "seconds")
    # main()
