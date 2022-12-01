print(max(list(map(lambda l: sum(l), [list(map(int, s.strip().split('\n'))) for s in open("input.txt", "r").read().split('\n\n') if s]))))

