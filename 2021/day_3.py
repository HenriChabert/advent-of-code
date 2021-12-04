import pdb
from aoc_day import AOCDay
import functools
import re
import copy as cp

class Day3(AOCDay):
    def __init__(self, filepath=None):
        self.day = 3
        super().__init__(filepath)
        self.inp = list(map(list, self.input_lines))
        self.inp_t = list(map(list, zip(*self.inp)))

    def solve_part_1(self):
        gamma_rate = int("".join([self.most_common_byte(x) for x in self.inp_t]), 2)
        epsilon_rate = int("".join([str(1 - int(x)) for x in str(bin(gamma_rate))[2:]]), 2)
        return gamma_rate * epsilon_rate

    def solve_part_2(self):
        oxygen_valid_numbers = cp.deepcopy(self.inp)
        co2_valid_numbers = cp.deepcopy(self.inp)
        for i in range(len(oxygen_valid_numbers[0])):
            most_common_byte = self.most_common_byte([n[i] for n in oxygen_valid_numbers], value_eq=1)
            least_common_byte = self.least_common_byte([n[i] for n in co2_valid_numbers], value_eq=0)
            oxygen_valid_numbers = [n for n in oxygen_valid_numbers if n[i] == most_common_byte or len(oxygen_valid_numbers) == 1]
            co2_valid_numbers = [n for n in co2_valid_numbers if n[i] == least_common_byte or len(co2_valid_numbers) == 1]
        return int("".join(oxygen_valid_numbers[0]), 2) * int("".join(co2_valid_numbers[0]), 2)

    @staticmethod
    def most_common_byte(s, value_eq=0):
        return str(max(['0', '1'] if value_eq == 0 else ['1', '0'], key=s.count))

    @staticmethod
    def least_common_byte(s, value_eq=0):
        return str(min(['0', '1'] if value_eq == 0 else ['1', '0'], key=s.count))

if __name__ == "__main__":
    # day = Day3(filepath="inputs/day_3.txt")
    day = Day3()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")