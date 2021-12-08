data = open('2021\day03\input.txt', "r").readlines()

# part 1
gamma = epsilon = ""
for i in range(len(data[0])):
    col = [row[i] for row in data]
    gamma += max(set(col), key=col.count)
    epsilon += min(set(col), key=col.count)

#binary conversion
int_max= int(gamma, 2)
int_min= int(epsilon, 2)
part1 = int_max * int_min

# part 2 
def reduce_codes(codes, maximize, alt):
    for i in range(len(codes[0])):
        col = [row[i] for row in codes]
        gamma = epsilon = ""
        gamma += max(set(col), key=col.count)
        epsilon += min(set(col), key=col.count)
        match = gamma if maximize else epsilon
        if gamma != epsilon:
            codes = [x for x in codes if x[i] == match]
        else:
            codes = [x for x in codes if x[i] == alt]
        if len(codes) == 1:
            return "".join(codes)

def Main():
    oxygen = reduce_codes(data, True, "1")
    co2 = reduce_codes(data, False, "0")
    part2 = int(oxygen, 2) * int(co2, 2)

    # answers
    print("Part 1:", part1)
    print("Part 2:", part2)    

if __name__ == '__main__':
    Main()