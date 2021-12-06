from dataclasses import dataclass
from copy import deepcopy
import math

def parse_input(input):
    lines = [line.replace(" ", "").split("->") for line in input.splitlines()]
    segments = []
    for unparsed_segment in lines:
        segment = LineSegment()
        segment.x1, segment.y1 = [int(p) for p in unparsed_segment[0].split(",")]
        segment.x2, segment.y2 = [int(p) for p in unparsed_segment[1].split(",")]
        segments.append(segment)
    x_bounds = max([s.x_max for s in segments]) + 1
    y_bounds = max([s.y_max for s in segments]) + 1
    diagram = [[0] * x_bounds for _ in range(y_bounds)]
    return diagram, segments


@dataclass
class LineSegment:
    x1: int = 0
    x2: int = 0
    y1: int = 0
    y2: int = 0

    @property
    def y_max(self):
        return max(self.y1, self.y2)

    @property
    def x_max(self):
        return max(self.x1, self.x2)

    @property
    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    @property
    def manhattan_distance(self):
        return (abs(self.x1 - self.x2) + abs(self.y1 - self.y2)) // 2

    def __repr__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

    def mark(self, diagram, include_diagonals=False):
        if self.is_diagonal and not include_diagonals:
            print("Skipping diagonal segment.")
            return
        if not self.is_diagonal:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                    diagram[y][x] += 1
        else:  # is diagonal
            dx = 1 if self.x1 < self.x2 else -1
            dy = 1 if self.y1 < self.y2 else -1
            curr_x = self.x1
            curr_y = self.y1
            for _ in range(self.manhattan_distance + 1):
                diagram[curr_y][curr_x] += 1
                curr_x += dx
                curr_y += dy


def print_diagram(d):
    for row in d:
        print(row)


def count_diagram(d):
    return sum([1 for x in range(len(d)) for y in range(len(d[0])) if d[x][y] >= 2])


def part1(diagram, segments):
    for s in segments:
        s.mark(diagram, include_diagonals=False)
    # print_diagram(diagram)
    return count_diagram(diagram)


def part2(diagram, segments):
    for s in segments:
        s.mark(diagram, include_diagonals=True)
    # print_diagram(diagram)
    return count_diagram(diagram)

if __name__ == "__main__":
    with open("2021/day05/input.txt", "r") as f:
        diagram, segments = parse_input(f.read())
    # part 1
    p1 = part1(deepcopy(diagram), segments)
    # part 2
    p2 = part2(deepcopy(diagram), segments)
    print(f"Part 1: {p1}\nPart 2: {p2}")