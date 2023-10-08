import argparse
import os
import pandas as pd

pwd = os.getcwd()
os.chdir(pwd)

parser = argparse.ArgumentParser(description="xlsx process tool")

parser.add_argument("-p", "--path", type=str, nargs=1, help="file path to operate")
parser.add_argument("-n", "--number", type=int, nargs=1, help="the column to delete")

args = parser.parse_args()

try:
    file = pd.read_excel(args.path[0])
    dColumn = file.columns[args.number[0]]
    file.drop(file.columns[args.number[0]], axis=1, inplace=True)
    file.to_excel(args.path[0])
    print("Successfully drop column", dColumn)
except PermissionError:
    print("Execute failed.")
    print("Permission Denied: check if the file is being used by other program")
except FileNotFoundError:
    print("Execute failed.")
    print("FileNotFound: check if the file exists")
except IndexError:
    print("Execute failed.")
    print("Index error: check if the column number is valid")


    

