from collections import Counter

def occurence_counter(s):
    return Counter(list(s.replace(" ", "")))

def occurence_pattern(s, ctr):
    return tuple(sorted([ctr[x] for x in s]))

def translation():
    canonical_pattern = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
    canonical_dict = occurence_counter(canonical_pattern)

    translator = {}
    for i, x in enumerate(canonical_pattern.split(" ")):
        translator[occurence_pattern(x, canonical_dict)] = i
    return translator

def process_line(ls):
    outputs = ls[1].strip()
    occ_dict = occurence_counter(ls[0])
    return [translation()[occurence_pattern(x, occ_dict)] for x in outputs.split(" ")]

def Main():
    data = [x.strip().split("|") for x in open("2021/day08/input.txt").readlines()]
    part_one = 0
    part_two = 0
    for line in data:
        p = process_line(line)
        part_one += len([x for x in p if x in [1, 4, 7, 8]])
        part_two += int("".join([str(x) for x in p]))
    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")

if __name__ == '__main__':
    Main()