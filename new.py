import concurrent.futures
import time
import pandas as pd
from collections import Counter

lines = []
with open("./test","r") as test:
    line = test.readline()
    while line:
        lines.append(line.rstrip("\n"))
        line = test.readline()


with open("./test","r+") as test:
    for line in lines:
        test.write(f"{line}-python\n")
    
    