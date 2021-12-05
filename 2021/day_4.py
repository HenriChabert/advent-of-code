import pdb
from aoc_day import AOCDay
import copy as cp

class Day4(AOCDay):
    def __init__(self, filepath=None):
        self.day = 4
        super().__init__(filepath)
        self.draw_list = list(map(int, self.input_lines[0].split(",")))
        self.boards = [[list(map(int, y.split())) for y in x.split("\n")] for x in self.raw_input.split("\n\n")[1:]]

    def calc_boards_score(self):
        boards_score = []
        list_score = lambda l: int(max(l, key=lambda x: self.draw_list.index(x))) if not len(set(l).difference(set(self.draw_list))) else -1
        for i, b in enumerate(self.boards):
            max_score = (0, 1000)
            b_t = list(map(list, zip(*b)))
            for r in b:
                score = list_score(r)
                score_index = self.draw_list.index(score) if score >= 0 else 1000
                if score >= 0 and score_index < max_score[1]:
                    max_score = (score, score_index, i)
            for r in b_t:
                score = list_score(r)
                score_index = self.draw_list.index(score) if score >= 0 else 1000
                if score >= 0 and score_index < max_score[1]:
                    max_score = (score, score_index, i)
            boards_score.append(max_score)

    def solve_part_1(self):
        best_board_score = min(self.calc_boards_score(), key=lambda x: x[1])
        return best_board_score[0]*sum(set(sum(self.boards[best_board_score[2]], [])).difference(set(self.draw_list[:best_board_score[1]+1])))
        

    def solve_part_2(self):
        best_board_score = max(self.calc_boards_score(), key=lambda x: x[1])
        return best_board_score[0]*sum(set(sum(self.boards[best_board_score[2]], [])).difference(set(self.draw_list[:best_board_score[1]+1])))


if __name__ == "__main__":
    # day = Day4(filepath="inputs/day_4_sample.txt")
    day = Day4()
    print(f"Part 1: {day.solve_part_1()}")
    print(f"Part 2: {day.solve_part_2()}")