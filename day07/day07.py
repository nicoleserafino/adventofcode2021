import pandas as pd

def fuel_calc(align_pos, part):
    if part == 1:
        return int(abs(df['a'] - align_pos).sum())
    if part == 2:
        return int((0.5 * abs(df['a'] - align_pos) * (abs(df['a'] - align_pos) + 1)).sum())


def minimum_fuel_consumed(part):
    n = round(df['a'].mean())
    lowest_fuel = fuel_calc(n, part)
    while lowest_fuel > fuel_calc(n + 1, part) and n + 1 < df['a'].max():
        n = n + 1
        lowest_fuel = fuel_calc(n, part)
    while lowest_fuel > fuel_calc(n - 1, part) and n > 0:
        n = n - 1
        lowest_fuel = fuel_calc(n, part)
    return lowest_fuel

if __name__ == '__main__':
    file = open("2021/day07/input.txt").read()
    data = list(map(int, file.split(',')))
    df = pd.DataFrame(data, columns=['a'])

    print('Part 1:', minimum_fuel_consumed(1))
    print('Part 2:', minimum_fuel_consumed(2))