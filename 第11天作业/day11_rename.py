import threading
import os

# names = ["a","b","c","d","e","f","g","h","i","j","k"]
names = [f"{i}.txt" for i in range(20)]
filespath = "./testfiles"
files = os.listdir(filespath)

lock = threading.Lock()


def renameWorker(oldpath, newpath):
    lock.acquire()
    try:
        os.rename(oldpath, newpath)
        print(oldpath, "<- old")
        print(f"{os.path.basename(oldpath)} has been renamed to {os.path.basename(newpath)}")
    except:
        print("rename failed")
    finally:
        lock.release()


i = 0
threadlist = []
for file in files:
    newname = names[i]
    i += 1
    renamethread = threading.Thread(target=renameWorker, args=(f"{filespath}/{file}", f"{filespath}/{newname}"))
    threadlist.append(renamethread)
    renamethread.start()

for t in threadlist:
    t.join()