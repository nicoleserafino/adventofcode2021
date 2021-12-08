from functools import partial, reduce


def draw_num(boards, draws, idx=0):
    for i, board in enumerate(boards):
        if -5 in map(sum, board) or -5 in map(sum, zip(*board)):
            return idx - 1, i, board
    return draw_num([update_board(draws[idx], x) for x in boards], draws, idx + 1)


def board_sum(board):
    return sum([x for x in reduce(lambda x, y: x + y, board) if x != -1])


def update_board(num, board):
    return [[-1 if x == num else x for x in row] for row in board]


def parse_input(data):
    seq = [[int(y) for y in x.split()] for x in data if x != "\n"]
    return [seq[i:i+5] for i, x in enumerate(seq) if i % 5 == 0]

def Main():
    with open("2021/day04/input.txt", 'r') as f:
        draws = [int(x) for x in f.readline().split(",")]
        boards = parse_input(f.readlines())

    # PART 1
    draw_idx, _, win_board = draw_num(boards, draws)
    print("Part 1:", draws[draw_idx] * board_sum(win_board))

    # PART 2
    draw_idx = 0
    while boards:
        draw_idx, win_idx, win_board = draw_num(boards, draws)
        del boards[win_idx]
    print("Part 2:", draws[draw_idx] * board_sum(win_board)) 
    
if __name__ == '__main__':
    Main()