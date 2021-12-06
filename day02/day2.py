data = open('2021\day02\input.txt', "r").readlines()

horizontal = 0
depth = 0
depthPt2 = 0
aim = 0

for i in data:
    direction = i.split(" ")[0]
    amt = int(i.split(" ")[1])

    if direction == "forward":
        horizontal += amt
        depthPt2 += aim * amt
    elif direction == "down":
        depth += amt
        aim += amt
    elif direction == "up":
        depth -= amt
        aim -= amt
    else:
        print("error")

print("Part 1:", horizontal * depth)
print("Part 2:", horizontal * depthPt2)
