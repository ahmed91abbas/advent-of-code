with open("data.in", "r") as f:
    lines = f.readlines()


class Node:
    def __init__(self, x, y, c, max_x, max_y):
        self.x = x
        self.y = y
        self.c = c
        self.max_x = max_x
        self.max_y = max_y
        self.neighbors_indices = self.get_neighbors_indices()

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.c})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return self.c

    def get_neighbors_indices(self):
        indices = []
        if self.c == "|":
            if self.y > 0:
                indices.append((self.x, self.y - 1))
            if self.y < self.max_y:
                indices.append((self.x, self.y + 1))
        elif self.c == "-":
            if self.x > 0:
                indices.append((self.x - 1, self.y))
            if self.x < self.max_x:
                indices.append((self.x + 1, self.y))
        elif self.c == "L":
            if self.y > 0:
                indices.append((self.x, self.y - 1))
            if self.x < self.max_x:
                indices.append((self.x + 1, self.y))
        elif self.c == "J":
            if self.y > 0:
                indices.append((self.x, self.y - 1))
            if self.x > 0:
                indices.append((self.x - 1, self.y))
        elif self.c == "7":
            if self.y < self.max_y:
                indices.append((self.x, self.y + 1))
            if self.x > 0:
                indices.append((self.x - 1, self.y))
        elif self.c == "F":
            if self.y < self.max_y:
                indices.append((self.x, self.y + 1))
            if self.x < self.max_x:
                indices.append((self.x + 1, self.y))
        return indices


"""
-----> x
|
|
>
y
"""
graph = {}
start_node = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != "\n":
            node = Node(x, y, c, len(line) - 1, len(lines) - 1)
            if c == "S":
                start_node = node
            graph[(x, y)] = node

s_neighbors_indices = []
if (start_node.x - 1, start_node.y) in graph and graph[(start_node.x - 1, start_node.y)].c in ["-", "F", "L"]:
    s_neighbors_indices.append((start_node.x - 1, start_node.y))
if (start_node.x + 1, start_node.y) in graph and graph[(start_node.x + 1, start_node.y)].c in ["-", "7", "J"]:
    s_neighbors_indices.append((start_node.x + 1, start_node.y))
if (start_node.x, start_node.y - 1) in graph and graph[(start_node.x, start_node.y - 1)].c in ["|", "F", "7"]:
    s_neighbors_indices.append((start_node.x, start_node.y - 1))
if (start_node.x, start_node.y + 1) in graph and graph[(start_node.x, start_node.y + 1)].c in ["|", "L", "J"]:
    s_neighbors_indices.append((start_node.x, start_node.y + 1))

graph[(start_node.x, start_node.y)].neighbors_indices = s_neighbors_indices

assert len(s_neighbors_indices) == 2

start = graph[(s_neighbors_indices[0][0], s_neighbors_indices[0][1])]
end = graph[(s_neighbors_indices[1][0], s_neighbors_indices[1][1])]


queue = [(start, 0, [start])]
visited = set()

while queue:
    node, steps, path = queue.pop(0)

    if node == end:
        # print("Path:", path)
        # print("Length:", steps)
        break

    if node not in visited:
        visited.add(node)

        for neighbor in node.neighbors_indices:
            if graph[neighbor].c not in ["S", "."]:
                new_path = path + [graph[neighbor]]
                queue.append((graph[neighbor], steps + 1, new_path))

# Get polygon area (shoelace formula)
area = 0
for i in range(len(path)):
    area += (path[i - 1].x + path[i].x) * (path[i - 1].y - path[i].y)
inside = (abs(area) - len(path) + 2) // 2

print(inside)
