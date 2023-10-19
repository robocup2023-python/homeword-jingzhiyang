from typing import *
from itertools import permutations


# no1
def threedigit(num: int, times: int) -> Generator[str, None, None]:
    for t in permutations(range(1, num + 1), times):
        numbers: List[str] = []
        for i in t:
            numbers.append(str(i))
        yield "".join(numbers)


print(*list(threedigit(4, 3)))


# no2
def getsort() -> List[int]:
    words: str = input("Enter 3 num: ")
    word: List[str] = words.split()
    ans: List[int] = []
    for i in range(len(word)):
        ans.append(int(word[i]))
    ans.sort()
    return ans


print(*getsort())


# no3
def fib(times: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for i in range(times):
        yield a
        a, b = b, a + b


print(*list(fib(20)))


# no4
def multiplication_table() -> None:
    i: int
    j: int
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{i}*{j}={i * j}", end=' ')
        print()

multiplication_table()
