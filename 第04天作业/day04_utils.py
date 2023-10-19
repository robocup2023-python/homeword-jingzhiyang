from itertools import starmap
import random
from pprint import pp

print(",".join(map(str, [1, 2, 3, 4, 5])))

test = list(range(21))
num = int(random.random() * 200) / 10
print(num)


# Inserting an element using binary search.
def binaryinsert(target, num):
    low = 0
    high = len(target)
    while low < high:
        mid = (low + high) // 2
        if target[mid] > num:
            high = mid
        else:
            low = mid + 1
    target.insert(low, num)


binaryinsert(test, num)
print(test)

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def addmatrix(m1, m2):
    return list(starmap(lambda x, y: list(starmap(lambda a, b: a + b, zip(x, y))), zip(m1, m2)))


pp(addmatrix(m1, m2))


def moveitem(target, m):
    n = len(target)
    return target[n - m:] + target[:n - m]


test = list(range(30))
print(moveitem(test, 5))


list = list(range(30))
for idx in range(len(list)-1,-1,-1):
    if list[idx] % 2 == 1:
        list.pop(idx)
print(list)



