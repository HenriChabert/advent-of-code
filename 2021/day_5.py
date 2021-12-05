import pdb
from aoc_day import AOCDay
import copy as cp

class Grid:
    def __init__(self):
        self.grid = {}
    
    def draw_line(self, c1, c2, ignore_diag=False):
        if not (self.is_diag(c1, c2) and ignore_diag):
            x1, y1 = c1
            x2, y2 = c2
            d = abs(x2 - x1) or abs(y2 - y1)
            for i in range(d + 1):
                x = int((x2 - x1)/d)*i + x1 if x1 != x2 else x1
                y = int((y2 - y1)/d)*i + y1 if y1 != y2 else y1
                self.grid[(x, y)] = self.grid.get((x, y), 0) + 1
    
    def is_diag(self, c1, c2):
        return abs(c1[0]-c2[0]) == abs(c1[1]-c2[1])

    def get_n_intersection(self):
        return len([x for x in self.grid.values() if x > 1])

class Day5(AOCDay):
    def __init__(self, filepath=None):
        self.day = 5
        super().__init__(filepath)
        self.inp = [[tuple(map(int, y.split(","))) for y in x.split(" -> ")] for x in self.input_lines]
        

    def solve_part_1(self):
        grid = Grid()
        for line in self.inp:
            grid.draw_line(line[0], line[1], ignore_diag=True)
        return grid.get_n_intersection()

    def solve_part_2(self):
        grid = Grid()
        for line in self.inp:
            grid.draw_line(line[0], line[1])
        return grid.get_n_intersection()

if __name__ == "__main__":
    day = Day5(filepath="inputs/day_5.txt")
    # day = Day5()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")