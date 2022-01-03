from functools import cache

def play1(pos1, pos2, score1=0, score2=0, i=0):
    if score2 >= 1000: return i*score1
    pos1 = (pos1 + 3*i+6) % 10 or 10
    return play1(pos2, pos1, score2, score1+pos1, i+3)

@cache
def play2(pos1, pos2, score1=0, score2=0):
    if score2 >= 21: return 0, 1

    wins1, wins2 = 0, 0
    for move, n in (3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1):
        pos1_ = (pos1 + move) % 10 or 10
        w2, w1 = play2(pos2, pos1_, score2, score1 + pos1_)
        wins1, wins2 = wins1 + n*w1, wins2 + n*w2
    return wins1, wins2
    
def Main():
    pos1, pos2 = [int(x.split()[-1]) for x in open("2021/day21/input.txt")]

    part1 = play1(pos1, pos2)
    part2 = max(play2(pos1, pos2))

    print(f'Part 1: {part1}\nPart 2: {part2}')
if __name__ == '__main__':
    Main()