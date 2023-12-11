from itertools import combinations

with open("data.in", "r") as f:
    graph = [list(line.strip()) for line in f.readlines()]

flipped_graph = list(map(list, zip(*graph)))
extra_rows = [i for i, line in enumerate(graph) if "#" not in line]
extra_columns = [i for i, line in enumerate(flipped_graph) if "#" not in line]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


galaxies = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == "#":
            galaxies.append(Node(i, j))

pairs = combinations(galaxies, 2)
result = 0
for pair in pairs:
    for extra_row in extra_rows:
        if min(pair[0].x, pair[1].x) < extra_row < max(pair[0].x, pair[1].x):
            result += 1000000 - 1
    for extra_column in extra_columns:
        if min(pair[0].y, pair[1].y) < extra_column < max(pair[0].y, pair[1].y):
            result += 1000000 - 1
    result += abs(pair[0].x - pair[1].x) + abs(pair[0].y - pair[1].y)
print(result)
