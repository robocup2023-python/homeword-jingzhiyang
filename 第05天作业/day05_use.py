import shutil
from typing import *
from itertools import filterfalse
from PIL import Image
import os
import random


# cacluate the average number of the numbers
def caclcuate(*args) -> tuple:
    sum = 0
    for i in args:
        sum += i
    index = [i for i in range(0, len(args)) if args[i] > sum / len(args)]
    return sum / len(args), index


print(caclcuate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def getodd(*args):
    return filterfalse(lambda x: x % 2 == 0, args)


print(*list(getodd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))


def createrandom():
    with open("./test.txt", "w") as file:
        for k in range(100000):
            file.write(f"{random.randint(1, 100)}\n")


createrandom()


def createimage():
    if os.path.exists("./img"):
        shutil.rmtree("./img")
    os.makedirs("./img")
    for t in range(100):
        image = Image.new("RGB", (1, 1), tuple(random.randint(0, 254) for i in range(3)))
        image.save(f"./img/{t:02X}.png")


createimage()


def changename():
    names = os.listdir("./img")
    for name in random.sample(names, len(names) // 2):
        os.rename(f"./img/{name}", f"./img/{name.rstrip('.png')}.jpg")

changename()
