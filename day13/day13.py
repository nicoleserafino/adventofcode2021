# fold dots according to the axis, 'x' or 'y', and the distance d
def fold(dots, axis, d):
    folded = []
    for x,y in dots:
        if axis == 'x' and x > d:
            x = 2*d - x
        if axis == 'y' and y > d:
            y = 2*d - y
        if (x,y) not in folded:
            folded.append((x,y))
    return folded

# print the dots
def print_dots(dots):
    dots.sort() # sort by x first
    xmax = dots[-1][0]
    dots.sort(key=lambda dots: dots[1]) # sort by y
    ymax = dots[-1][1]

    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if dots and dots[0] == (x,y):
                print('#', end='')
                dots.pop(0)
            else:
                print(' ', end='')
        print()

def parse_data(data):
    instructions = []
    dots = []
    line = data.readline()
    while line != '':
        p = line.strip().split(',')
        if len(p) == 2:
            dots.append( (list(map(int, p))) )
        else:
            q = line.strip().split()
            if len(q) == 3:
                r = q[2].split('=')
                instructions.append( (r[0], int(r[1])) )
        line = data.readline()
    return instructions, dots

def Main():
    instructions, dots = parse_data(open("2021/day13/input.txt"))
    # Part 1: fold once
    axis, d = instructions.pop(0)
    dots = fold(dots, axis, d)
    print(f"Part 1: {len(dots)}")

    # Part 2: perform the remaining foldings
    for axis, d in instructions:
        dots = fold(dots, axis, d)

    print("Part 2:")
    print_dots(dots)

if __name__ == "__main__":
    Main()
