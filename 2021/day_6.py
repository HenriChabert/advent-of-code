import pdb
from aoc_day import AOCDay
import copy as cp
# Draw the graph
import matplotlib.pyplot as plt
import numpy as np

DELIVER_TIME = 7

class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

    def deliver(self):
        self.timer = DELIVER_TIME - 1

    def __repr__(self):
        return f"Lanternfish({self.timer})"

    def __str__(self):
        return f"Lanternfish({self.timer})"

class LanternfishSchool:
    def __init__(self, lanternfish_list):
        self.lanternfish_list = cp.copy(lanternfish_list)

    def tick(self):
        for i in range(len(self.lanternfish_list)):
            self.lanternfish_list[i].timer -= 1
            if self.lanternfish_list[i].timer == -1:
                self.lanternfish_list[i].deliver()
                self.lanternfish_list.append(Lanternfish(DELIVER_TIME + 1))

class Day6(AOCDay):
    def __init__(self, filepath=None):
        self.day = 6
        super().__init__(filepath)
        self.inp = list(map(int, self.input_lines[0].split(',')))
        
    def run_scenario(self, lanternfishes, n_ticks):
        print("Running scenario with {} ticks".format(n_ticks))
        lf_school = LanternfishSchool(lanternfishes)
        for i in range(n_ticks):
            lf_school.tick()
        return len(lf_school.lanternfish_list)

    def solve_part_1(self):
        lanternfishes= [Lanternfish(lf) for lf in self.inp]
        return self.run_scenario(lanternfishes, 80)

    def solve_part_2(self):
        N_TICKS = 256
        school = [self.inp.count(i) for i in range(9)]
        for _ in range(N_TICKS):
            parents = school[0]
            for fish_group_i in range(len(school) - 1):
                school[fish_group_i] = school[fish_group_i + 1]
            school[6] += parents
            school[8] = parents
        return sum(school)


if __name__ == "__main__":
    # day = Day6(filepath="inputs/day_6_sample.txt")
    day = Day6()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")

    