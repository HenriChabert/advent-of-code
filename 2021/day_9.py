import pdb
from aoc_day import AOCDay
import copy as cp
# Draw the graph
import numpy as np
import functools

class Day9(AOCDay):
    def __init__(self, filepath=None):
        self.day = 9
        super().__init__(filepath)
        self.inp = [list(map(int, list(x))) for x in self.input_lines]

    def get_height(self, x, y):
        return int(self.inp[x][y]) if x < len(self.inp) and y < len(self.inp[x]) and x >= 0 and y >= 0 else np.inf

    def find_low_points(self):
        low_points = []
        for x in range(len(self.inp)):
            for y in range(len(self.inp[x])):
                v = int(self.inp[x][y])
                if v < self.get_height(x, y - 1) and v < self.get_height(x, y + 1) and v < self.get_height(x - 1, y) and v < self.get_height(x + 1, y):
                    low_points.append((x, y))
        return low_points

    def find_bassin_size(self, i, j, visited, v):
        if (i, j) in visited:
            return 0
        if i < 0 or j < 0 or i >= len(self.inp) or j >= len(self.inp[0]) or self.inp[i][j] == 9:
            visited.append((i, j))
            return 0
        if self.inp[i][j] < v :
            return 0
        visited.append((i, j))
        sm = 1
        sm += self.find_bassin_size(i+1, j, visited, self.inp[i][j])
        sm += self.find_bassin_size(i-1, j, visited, self.inp[i][j])
        sm += self.find_bassin_size(i, j+1, visited, self.inp[i][j])
        sm += self.find_bassin_size(i, j-1, visited, self.inp[i][j])
        return sm

    def solve_part_1(self):
        low_points = self.find_low_points()
        return sum([int(self.inp[x][y]) + 1 for x, y in low_points])

    def solve_part_2(self):
        low_points = self.find_low_points()
        bassin_sizes = []
        for lp in low_points[1:]:
            bassin_size = self.find_bassin_size(lp[0], lp[1], [], -1)
            bassin_sizes.append(bassin_size)
        return functools.reduce(lambda a, b: a*b, list(sorted(bassin_sizes, reverse=True))[:3])



if __name__ == "__main__":
    # day = Day9(filepath="inputs/day_9_sample.txt")
    day = Day9()
    # print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")


        