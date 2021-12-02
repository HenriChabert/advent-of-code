import pdb
from aoc_day import AOCDay
import functools
import re

class Day2(AOCDay):
    def __init__(self, filepath=None):
        self.day = 2
        super().__init__(filepath)
        self.inp = list(map(lambda x: x.split(), self.input_lines))

    def solve_part_1(self):
        return functools.reduce(lambda a, b: a*b, functools.reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), [(int(e[1]) if e[0] == "forward" else 0, int(e[1])*(1 - 2*(e[0] == "up") if e[0] != "forward" else 0)) for e in self.inp]))

    def solve_part_2(self):
        aim = 0
        c = (0, 0)
        for e in self.inp:
            if e[0] != "forward":
                aim += int(e[1])*(1 - 2*(e[0] == "up"))
            else:
                c = (c[0] + int(e[1]), c[1] + int(e[1])*aim)
        return c[0] * c[1]

if __name__ == "__main__":
    # day = Day2(filepath="inputs/day_2_sample.txt")
    day = Day2()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")