from collections import defaultdict

# I am not proud of this parsing but I finished in the top 1000 people sooo
def parse_data(data):
    adj_list = defaultdict(list)
    small_caves = set()
    for line in data:
        edge = line.strip().split('-')
        a, b = edge[0], edge[1]
        adj_list[a].append(b)
        adj_list[b].append(a)

        if (a.lower() == a):
            small_caves.add(a)
        if (b.lower() == b):
            small_caves.add(b)
    return adj_list, small_caves

def find_paths(current, visited):
    if current in visited:
        return 0

    if current == 'end':
        return 1
    
    if current in small_caves:
        visited.add(current)

    total_paths = 0

    for neighbor in adj_list[current]:
        total_paths += find_paths(neighbor, visited)
    
    visited.discard(current)
    
    return total_paths

def find_paths2(current, visited, visited_small_twice):
    if current == 'end':
        return 1
    
    if visited[current] > 0 and visited_small_twice:
        return 0
    
    if current in small_caves:
        visited[current] += 1
        visited_small_twice |= visited[current] == 2

    total_paths = 0

    for neighbor in adj_list[current]:
        if neighbor != 'start':
            total_paths += find_paths2(neighbor, visited, visited_small_twice)
            
    visited[current] -= 1
    
    return total_paths

def Main():
    global adj_list, small_caves
    file = open('2021/day12/input.txt', 'r')
    adj_list, small_caves = parse_data(file)    

    print(f"Part 1: {find_paths('start', set())}\nPart 2: {find_paths2('start', defaultdict(int), False)}")

if __name__ == '__main__':
    Main()