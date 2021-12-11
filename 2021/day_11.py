import pdb
from aoc_day import AOCDay
import copy as cp
# Draw the graph
import numpy as np
import functools

class Octopus:
    def __init__(self, i, j, garden, energy):
        self._energy = energy
        self.garden = garden
        self.x = i
        self.y = j
        self._lock = False

    def power_up(self):
        if not self._lock:
            self._energy += 1
            if self._energy >= 10:
                self.flash()

    def flash(self):
        self._lock = True
        self.garden.has_flashed(self)
        self._energy = 0

    def is_locked(self):
        return self._lock

    def unlock(self):
        self._lock = False

    def __repr__(self):
        return str(self._energy)

    def __str__(self):
        return str(self._energy)

class OctopusGarden:
    def __init__(self, octopuses=None):
        self.garden = octopuses
        self.flashes_cpt = 0

    def from_list(self, oct_list):
        self.garden = [[Octopus(i, j, self, oct_list[i][j]) for j in range(len(oct_list[i]))] for i in range(len(oct_list))]

    def get_neighbours(self, octopus):
        return [self.garden[octopus.x + i][octopus.y + j] for i in (-1, 0, 1) for j in (-1, 0, 1) if octopus.x + i >= 0 and octopus.y + j >= 0 and octopus.x + i < len(self.garden) and octopus.y + j < len(self.garden[0]) and (i != 0 or j != 0) and not self.garden[octopus.x + i][octopus.y + j].is_locked()]

    def has_flashed(self, octopus):
        for n in self.get_neighbours(octopus):
            n.power_up()
        self.flashes_cpt += 1

    def tick(self):
        for i in range (len(self.garden)):
            for j in range (len(self.garden[i])):
                self.garden[i][j].power_up()
        self.unlock_all()

    def unlock_all(self):
        for i in range (len(self.garden)):
            for j in range (len(self.garden[i])):
                self.garden[i][j].unlock()

    def all_flashed(self):
        return all([octopus._energy == 0 for l in self.garden for octopus in l])

    def __repr__(self):
        return str(self.garden)

    def __str__(self):
        return str(self.garden)


class Day11(AOCDay):
    def __init__(self, filepath=None):
        self.day = 11
        super().__init__(filepath)
        self.inp = [list(map(int, list(l))) for l in self.input_lines]

    def solve_part_1(self):
        octopus_garden = OctopusGarden()
        octopus_garden.from_list(self.inp)
        N_ITER = 100
        for _ in range(N_ITER):
            octopus_garden.tick()
        return octopus_garden.flashes_cpt
        
    def solve_part_2(self):
        octopus_garden = OctopusGarden()
        octopus_garden.from_list(self.inp)
        n = 0
        while not octopus_garden.all_flashed():
            octopus_garden.tick()
            n += 1
        return n
        




if __name__ == "__main__":
    # day = Day11(filepath="inputs/day_11_sample.txt")
    day = Day11()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")


        