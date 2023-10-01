# Python version of the Gonway's Game of Life
from random import randint
from typing import *
from time import sleep


# Run the code by `$ python ./day13_lifegame.py` in the terminal

# ==============Ordinary Solution==========================


class Universe:
    width: int
    height: int
    cells: List[List[str]]
    
    def __init__(self):
        self.width = 80
        self.height = 15
        self.cells = [[" "] * self.width for _ in range(self.height)]
        self.mark = "*"
        self.seed()
    
    def show(self):
        print("\x1b[H")
        for line in self.cells:
            for char in line:
                print(char, end="")
            print()
        print("\n\n\nPress `Enter` to continue,enter `q` to quit.")
     
    def seed(self):
        initialTotal = self.width * self.height // 10
        cnt = 0
        while cnt < initialTotal:
            i = randint(0, self.height - 1)
            j = randint(0, self.width - 1)
            if self.cells[i][j] != self.mark:
                cnt += 1
                self.cells[i][j] = self.mark
    
    def alive(self, i: int, j: int):
        if i < 0 or j < 0 or i >= self.height or j >= self.width or self.cells[i][j] == ' ':
            return False
        return True
    
    def neighbors(self, i: int, j: int):
        cnt = 0
        for Di, Dj in [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
            if self.alive(i + Di, j + Dj):
                cnt += 1;
        return cnt
    
    def next(self, i: int, j: int):
        nbCnt = self.neighbors(i, j)
        if self.alive(i, j):
            if nbCnt < 2 or nbCnt > 3:
                return False
            else:
                return True
        elif not self.alive(i, j) and nbCnt == 3:
            return True
        return False
    
    def step(self):
        chStatus = {}
        for i in range(self.height):
            for j in range(self.width):
                if self.alive(i, j) and not self.next(i, j):
                    chStatus[(i, j)] = " "
                elif not self.alive(i, j) and self.next(i, j):
                    chStatus[(i, j)] = self.mark
        for (posi, posj), value in chStatus.items():
            self.cells[posi][posj] = value


def bigBang():
    uni = Universe()
    print("\x1b[2J")
    while not (all([i == uni.mark for i in sum(uni.cells, [])]) or all([i == " " for i in sum(uni.cells, [])])):
        uni.show()
        uni.step()
        # sleep(20)
        c = input()
        if c == "q":
            print("game ends")
            break


if __name__ == "__main__":
    bigBang()
