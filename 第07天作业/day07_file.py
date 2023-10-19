import random
import os
import shutil

# Write
with open("./test.txt", "w") as file:
    for t in range(10):
        for j in range(3):
            file.write(f"{random.randint(1, 100):3d}")
        file.write("\n")


print("No1 problem complete")
c = input("Enter anything to continue: ")

# Insert
with open("./test.txt", "r+") as file:
    # origin = file.read()
    # file.seek(0)
    file.write("Python\n")
    # file.write(origin)
    # file.write("Python\n")

print("No2 problem complete")
c = input("Enter anything to continue: ")

# Compare
with open("./test.txt", "r") as file1, open("./test_copy.txt", "r") as file2:
    first, second = file1.readline(), file2.readline()
    index = 0
    print(f"Different at line: ")
    while first and second:
        if first != second:
            print(f"{index + 1}")
        index += 1
        first, second = file1.readline(), file2.readline()

print("No3 problem complete")
c = input("Enter anything to continue: ")

# no5
if os.path.exists("./test"):
    shutil.rmtree("./test")
os.makedirs("./test")
i,j = map(int,input("How many files and lines? (eg: 4 5): ").split())
for t in range(i):
    with open(f"./test/{t}.txt", "a") as file:
        for k in range(j):
            file.write(f"{random.randint(1,100):3d}\n")

print("No4 problem complete")
c = input("Enter anything to continue: ")

names = os.listdir("./test")
for name in names:
    lines = []
    with open(f"./test/{name}", "r+") as file:
        line = file.readline()
        while line:
            lines.append(line.rstrip("\n"))
            line = file.readline()
    
    with open(f"./test/{name}", "r+") as file:
        for line in lines:
            file.write(f"{line}-python\n")
            
    os.rename(f"./test/{name}", f"./test/{name.rstrip('.txt')}-python.txt")


print("No5 problem complete")
c = input("Enter anything to continue: ")

names = os.listdir("./test")
for name in names:
    if "python" in name:
        os.rename(f"./test/{name}", f"./test/{name.replace('python','class')}")
