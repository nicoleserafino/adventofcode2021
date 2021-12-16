def flash_count(data):
    xmax = len(data)
    ymax = len(data[0])
    total = xmax * ymax # total number of octopuses
    part1 = 100 # number of steps for part 1

    step_flashes = flashes  = 0 # cumulative number of flashes and flashes during one step
    glow = [] # all octopuses that glow and still have to be propagated

    step = 0 # step counter
    while step_flashes != total: # stop when the goal of part 2 is achieved
        step_flashes = 0
        # increase energy level of each octopus by 1
        for y in range(ymax):
            for x in range(xmax):
                # 9 + 1: starts to flash, becomes 0
                # remember for propagation
                if data[x][y] == 9:
                    data[x][y] = 0
                    glow.append((x,y))
                    step_flashes += 1
                # every other energy level is simply increased by 1
                else:
                    data[x][y] += 1

        # propagate to the adjacent 8 octopuses
        # keep doing it until all propagations have settled down
        while glow:
            # remove from the propagation list
            x,y = glow.pop()
            # increase the energy level of the adjacent octopuses
            for q in range(-1, 2):
                for p in range(-1, 2):
                    xn = x+p
                    yn = y+q
                    # don't change the center element
                    # stay within the bounds with xn, yn
                    if (p, q) != (0, 0) and 0 <= xn < xmax and 0 <= yn < ymax:
                        if data[xn][yn] == 9:
                            data[xn][yn] = 0
                            glow.append((xn,yn))
                            step_flashes += 1
                        # don't increase when already flashing (=0)
                        elif data[xn][yn] != 0:
                            data[xn][yn] += 1

        step += 1
        flashes += step_flashes
        if step == part1:
            p1 = flashes
    return p1, step

def Main():
    data = [[int(i) for i in line] for line in open("2021/day11/input.txt").read().splitlines()]
    p1, p2 = flash_count(data)
    print(f'Part 1: {p1}\nPart 2: {p2}')

if __name__ == '__main__':
    Main()