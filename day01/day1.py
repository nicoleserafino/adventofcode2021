data = [int(x) for x in open('2021\day01\input.txt', "r")]
print("Part 1:", sum([data[i] > data[i-1] for i in range(1, len(data))]))
print("Part 2:", sum([data[i] > data[i-3] for i in range(3, len(data))]))