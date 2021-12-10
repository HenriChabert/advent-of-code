import pdb
from aoc_day import AOCDay
import copy as cp
# Draw the graph
import numpy as np
import functools

class Day10(AOCDay):
    def __init__(self, filepath=None):
        self.day = 10
        super().__init__(filepath)
        self.md = {
            "[": "]",
            "{": "}",
            "(": ")",
            "<": ">"
        }

    def get_score_illegal(self, char):
        return {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137
        }[char]

    def get_score_incomplete(self, char):
        return {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4
        }[char]

    def illegal_char(self, s):
        pile = []
        for char in s:
            if char in self.md:
                pile.append(char)
            else:
                popel = pile.pop()
                if not self.md[popel] == char:
                    return self.md[popel], None
        return None, pile

    def solve_part_1(self):
        error_score = 0
        for line in self.input_lines:
            illegal_char = self.illegal_char(line)[0]
            if illegal_char:
                error_score += self.get_score_illegal(illegal_char)
        return error_score

    def solve_part_2(self):
        error_scores = []
        for line in self.input_lines:
            illegal_char, pile = self.illegal_char(line)
            if not illegal_char:
                error_scores.append(functools.reduce(lambda a, b: a*5 + self.get_score_incomplete(self.md[b]), reversed(pile), 0))
        return list(sorted(error_scores))[len(error_scores)//2]



if __name__ == "__main__":
    # day = Day10(filepath="inputs/day_10_sample.txt")
    day = Day10()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")


        