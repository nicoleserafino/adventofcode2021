def get_low_points(data):
    low_points = 0

    for i in range(len(data)):
        for j in range(len(data)):
            
            location = int(data[i][j])
            neighbors = {x:data[x[0]][x[1]] for x in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)] if -1 not in x and 100 not in x}

            if all([int(x) > location for x in list(neighbors.values())]):
                low_points += location + 1
    return low_points


def check_neighbors(data, basin_points, more_neighbors):
    all_neighbors = {}
    for k in more_neighbors.keys():
        i, j = k
        new_neighbors = {x:int(data[x[0]][x[1]]) for x in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)] if -1 not in x and 100 not in x and x not in basin_points.keys() and int(data[x[0]][x[1]]) != 9}
        all_neighbors = {**all_neighbors, **new_neighbors}
    return all_neighbors

def get_basins(data):
    basins_list = []
    for i in range(len(data)):
        for j in range(len(data)):
            starting_value = int(data[i][j])
            if (i,j) not in [basins_list[i][j][0] for i in range(len(basins_list)) for j in range(len(basins_list[i]))] and starting_value != 9:
                neighbors = {x:int(data[x[0]][x[1]]) for x in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)] if -1 not in x and 100 not in x and int(data[x[0]][x[1]]) != 9}
                basin_points = {**{(i,j): starting_value}, **neighbors}
                more_neighbors = check_neighbors(data, basin_points, neighbors)
                basin_points = {**basin_points, **more_neighbors}
                while more_neighbors != {}:
                    more_neighbors = check_neighbors(data, basin_points, more_neighbors)
                    basin_points = {**basin_points, **more_neighbors}
                basins_list.append(sorted(basin_points.items()))
            else:
                continue
    return sorted([len(x) for x in basins_list])[-1] * sorted([len(x) for x in basins_list])[-2] * sorted([len(x) for x in basins_list])[-3]

def Main():
    data = open("2021/day09/input.txt").read().splitlines()
    print("Part 1:", get_low_points(data))
    print("Part 2:", get_basins(data))

if __name__ == '__main__':
    Main()