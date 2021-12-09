import pdb
from aoc_day import AOCDay
import copy as cp
# Draw the graph
import matplotlib.pyplot as plt
import numpy as np

class Day7(AOCDay):
    def __init__(self, filepath=None):
        self.day = 7
        super().__init__(filepath)
        self.inp = list(map(int, self.input_lines[0].split(',')))

    def solve_part_1(self):
        median = np.median(self.inp)
        return int(sum([abs(x - median) for x in self.inp]))

    def solve_part_2(self): 
        mn = np.mean(self.inp)
        sum_crabs = lambda y: sum([abs(x - y)*(abs(x - y) + 1)//2 for x in self.inp])
        return min([sum_crabs(int(x)) for x in [mn-0.5, mn, mn+0.5]])


if __name__ == "__main__":
    day = Day7(filepath="inputs/day_7.txt")
    # day = Day7()
    # print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")