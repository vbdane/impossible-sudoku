'''
This is a fun script, not a serious repo. Please treat is as such.
I'm sure there are million ways to make it better.

'''

from checks import Checker
import random


class ImpossibleSudokuGenerator:

    def __init__(self):

        self.sudo = []
        self.empties = 0
        self.checking = Checker()

    def create(self):
        for i in range(9):
            self.sudo.append([])
            for j in range(9):
                self.sudo[i].append(0)

    def show(self):
        print("\n\t=== Impossible Sudoku ===\n")
        for i in range(9):
            print("\t",end="")
            for j in range(9):
                print(self.sudo[i][j], end="  ")
            print()
        print("\n\t {} blank spaces".format(self.empties))

    def linear_fill(self):
        for i in range(9):
            for j in range(9):
                if self.sudo[i][j] == 0:
                    pos = []
                    for n in range(1, 10):
                        res = self.checking.chkSeq(self.sudo, i, j, n)
                        if res is True:
                            pos.append(n)
                        else:
                            continue
                    pos_len = len(pos)
                    if pos_len > 1:
                        self.sudo[i][j] = pos[random.randint(0, pos_len - 1)]
                    elif pos_len == 1:
                        self.sudo[i][j] = pos[0]
                    else:
                        self.empties += 1

                else:
                    continue

    def generate(self):
        self.create()
        self.linear_fill()
        self.show()


if __name__ == '__main__':
    ImpossibleSudokuGenerator().generate()
