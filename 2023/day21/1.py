with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


class Node:
    def __init__(self, x, y, graph):
        self.x = x
        self.y = y
        self.graph = graph
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        neighbors = []
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = self.x + x
            new_y = self.y + y
            if 0 <= new_x < len(self.graph) and 0 <= new_y < len(self.graph[0]):
                if self.graph[new_x][new_y] != "#":
                    neighbors.append((new_x, new_y))
        return neighbors

    def __repr__(self):
        return (self.x, self.y)


graph = []
for line in lines:
    graph.append(list(line))

nodes = {}
start = None
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == ".":
            nodes[(i, j)] = Node(i, j, graph)
        elif graph[i][j] == "S":
            nodes[(i, j)] = Node(i, j, graph)
            start = nodes[(i, j)]

to_handle = {start}
for _ in range(64):
    new_to_handle = set()
    for node in to_handle:
        for neighbor in node.neighbors:
            new_to_handle.add(nodes[neighbor])
    to_handle = new_to_handle

print(len(to_handle))
