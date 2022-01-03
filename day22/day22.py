import math

def intersection(cube1, cube2):
    for a, b in zip(cube1, cube2):
        if a[0] > b[1] or a[1] < b[0]:
            return None

    return tuple((max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(cube1, cube2))

def difference(cube1, cube2):
    intsc = intersection(cube1, cube2)
    if not intsc:
        return [cube1]
    new_cubes = []
    new_cubes.append((cube1[0], cube1[1], (cube1[2][0], intsc[2][0] - 1)))
    new_cubes.append((cube1[0], cube1[1], (intsc[2][1] + 1, cube1[2][1])))
    new_cubes.append(((cube1[0][0], intsc[0][0] - 1), cube1[1], intsc[2]))
    new_cubes.append(((intsc[0][1] + 1, cube1[0][1]), cube1[1], intsc[2]))
    new_cubes.append((intsc[0], (cube1[1][0], intsc[1][0] - 1), intsc[2]))
    new_cubes.append((intsc[0], (intsc[1][1] + 1, cube1[1][1]), intsc[2]))

    return [(x, y, z) for x, y, z in new_cubes if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]

def solve(lines):
    cubes = []
    for line in lines:
        onoff = line[0]
        this_cube = line[1:]
        new_cubes = []
        for cube in cubes:
            new_cubes += difference(cube, this_cube)
        if onoff == 'on':
            new_cubes.append(this_cube)
        cubes = new_cubes

    s1 = s2 = 0
    for cube in cubes:
        s1 += math.prod(max(0, min(50, cube[i][1]) - max(-50, cube[i][0]) + 1) for i in range(3))
        s2 += math.prod(cube[i][1] - cube[i][0] + 1 for i in range(3))
    return s1, s2

def Main():
    lines = [(s.strip().split()[0], *[[int(x) for x in s.split()[1].split(',')[i].split('=')[1].split('..')] for i in range(3)]) for s in open('2021/day22/input.txt')]
    part1, part2 = solve(lines)
    print(f'Part 1: {part1}\nPart 2: {part2}')

if __name__ == '__main__':
    Main()

