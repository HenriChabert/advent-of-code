from aoc_day import AOCDay

class Day1(AOCDay):
    def __init__(self, filepath=None):
        self.day = 1
        super().__init__(filepath)
        self.inp = list(map(int, self.input_lines))

    def solve_part_1(self):
        return len([1 for i in range (len(self.inp)-1) if int(self.inp[i+1]) > int(self.inp[i])])

    def solve_part_2(self):
        return len([1 for i in range (len(self.inp)) if sum(self.inp[i:i+3]) < sum(self.inp[i+1:i+4])])

if __name__ == "__main__":
    day_1 = Day1()
    print(f"Part 1: {day_1.solve_part_1()}")
    print(f"Part 2: {day_1.solve_part_2()}")