import pandas as pd

file = pd.read_excel("./testdata.xlsx")
# del a line
file.drop(1,inplace=True)

#del a column
file.drop("2020-07",axis=1,inplace=True)

print(file.head())


