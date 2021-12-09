import pdb
from aoc_day import AOCDay
import copy as cp
# Draw the graph
import numpy as np

class Day8(AOCDay):
    def __init__(self, filepath=None):
        self.day = 8
        super().__init__(filepath)
        self.inputs = [x.split(" | ")[0].split() for x in self.input_lines]
        self.outputs = [x.split(" | ")[1].split() for x in self.input_lines]

    def solve_part_1(self):
        return len([y for x in self.outputs for y in x if y in x if len(y) in [2, 3, 4, 7]])

    def has_chars(self, s, l):
        return all([x in s for x in l])

    def get_key_from_value(self, d, val):
        return [k for k, v in d.items() if v == val][0]

    def solve_part_2(self):
        s = 0
        for inp_i, inp in enumerate(self.inputs):
            mp = {} 
            for d in inp:
                if len(d) == 2:
                    mp[1] = frozenset(d)
                elif len(d) == 3:
                    mp[7] = frozenset(d)
                elif len(d) == 4:
                    mp[4] = frozenset(d)
                elif len(d) == 7:
                    mp[8] = frozenset(d)
            
            mp[3] = frozenset(next(filter(lambda x: self.has_chars(x, mp[1]) and len(x) == 5, inp)))
            mp[9] = frozenset(next(filter(lambda x: self.has_chars(x, mp[4]) and len(x) == 6, inp)))
            mp[6] = frozenset(next(filter(lambda x: not self.has_chars(x, mp[7]) and len(x) == 6, inp)))
            mp[5] = frozenset(next(filter(lambda x: self.has_chars(mp[6], x) and len(x) == 5, inp)))
            mp[2] = frozenset(next(filter(lambda x: not self.has_chars(mp[6], x) and not self.has_chars(mp[9], x) and len(x) == 5, inp)))
            mp[0] = frozenset(next(filter(lambda x: not self.has_chars(x, mp[5]) and len(x) == 6, inp)))
            s += int("".join([str(self.get_key_from_value(mp, frozenset(x))) for x in self.outputs[inp_i]]))
        return s



if __name__ == "__main__":
    # day = Day8(filepath="inputs/day_8_sample.txt")
    day = Day8()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")


        