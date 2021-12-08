from collections import Counter

class School:
    def __init__(self, data: "list[int]"):
        self.fish = Counter(data)

    def update(self):
        self.fish = {k-1: v for k, v in self.fish.items()}
        self.fish[8] = self.fish.pop(-1, 0)
        if 6 in self.fish: self.fish[6] += self.fish[8]
        else: self.fish[6] = self.fish[8]

def count_fish(data, days):
    school = School(data)
    for i in range(days):
        school.update()
    return sum(school.fish.values())

def Main():
    # Return input data as list of strings
    data = [int(a) for a in open('2021/day06/input.txt').read().split(',')]
    # Part 1
    solution_1 = count_fish(data, 80)
    # Part 2
    solution_2 = count_fish(data, 256)
    # Report solution
    print(f'Part 1: {solution_1}\nPart 2: {solution_2}')

if __name__ == '__main__':
    Main()