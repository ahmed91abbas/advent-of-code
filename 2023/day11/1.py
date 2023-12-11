from itertools import combinations

with open("data.in", "r") as f:
    lines = f.readlines()

graph_list = []
n = 1
for i, line in enumerate(lines):
    graph_list.append([])
    for j, c in enumerate(line.strip()):
        if c == "#":
            graph_list[i].append(n)
            n += 1
        else:
            graph_list[i].append(0)

index = 0
while index < len(graph_list):
    row = graph_list[index]
    if sum(row) == 0:
        graph_list.insert(index, [0] * len(row))
        index += 1
    index += 1

col_to_expand = []
for i in range(len(graph_list[0])):
    col = [row[i] for row in graph_list]
    if sum(col) == 0:
        col_to_expand.append(i)

for row in graph_list:
    for i in sorted(col_to_expand, reverse=True):
        row.insert(i, 0)


class Node:
    def __init__(self, x, y, c, max_x, max_y):
        self.x = x
        self.y = y
        self.c = c
        self.max_x = max_x
        self.max_y = max_y
        self.neighbors_indices = self.get_neighbors_indices()

    def __repr__(self):
        return f"({self.x}, {self.y}): {self.c}"

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return str(self.c)

    def get_neighbors_indices(self):
        indices = []
        if self.y > 0:
            indices.append((self.x, self.y - 1))
        if self.y < self.max_y:
            indices.append((self.x, self.y + 1))
        if self.x > 0:
            indices.append((self.x - 1, self.y))
        if self.x < self.max_x:
            indices.append((self.x + 1, self.y))
        return indices


"""
-----> x
|
|
v
y
"""
graph = {}
galaxies = []
for i, row in enumerate(graph_list):
    for j, c in enumerate(row):
        node = Node(j, i, c, len(row) - 1, len(graph_list) - 1)
        graph[(j, i)] = node
        if c != 0:
            galaxies.append(node)

pairs = combinations(galaxies, 2)
result = 0
for pair in pairs:
    result += abs(pair[0].x - pair[1].x) + abs(pair[0].y - pair[1].y)
print(result)
