import concurrent.futures
import time
import pandas as pd
from collections import Counter

cnt = Counter({"a":1,"b":1})
test = pd.DataFrame(list(cnt.items()),columns=["ward","cnt"])
test.to_csv("./out.csv",index=None)



