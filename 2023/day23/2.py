with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


class Node:
    def __init__(self, x, y, max_x, max_y, tile):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.tile = tile
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if 0 <= x < self.max_x and 0 <= y < self.max_y:
                neighbors.append((x, y))
        return neighbors

    def __repr__(self):
        return str((self.x, self.y))


def get_longest_path(graph, start, end):
    longest_path = 0
    visited = set()

    def dfs(current, path_length):
        nonlocal longest_path
        if current == end:
            longest_path = max(longest_path, path_length)
        if current in visited or current not in graph:
            return
        visited.add(current)
        for neighbor in graph[current]:
            dfs(neighbor, graph[current][neighbor] + path_length)
        visited.remove(current)

    dfs(start, 0)
    return longest_path


start = None
end = None
graph = {}
for y, line in enumerate(lines):
    for x, tile in enumerate(line):
        if y == 0 and tile == ".":
            start = (x, y)
        elif y == len(lines) - 1 and tile == ".":
            end = (x, y)
        if tile != "#":
            graph[(x, y)] = Node(x, y, len(lines[0]), len(lines), tile)

interesting_nodes = [start, end]
for node in graph.values():
    if len([x for x in node.neighbors if x in graph]) >= 3:
        interesting_nodes.append((node.x, node.y))

new_graph = {point: {} for point in interesting_nodes}

for ix, iy in interesting_nodes:
    stack = [(ix, iy, 0)]
    seen = {(ix, iy)}
    while stack:
        x, y, dist = stack.pop()
        if dist != 0 and (x, y) in interesting_nodes:
            new_graph[(ix, iy)][(x, y)] = dist
            continue
        for neighbor in graph[(x, y)].neighbors:
            if neighbor in graph and neighbor not in seen:
                stack.append((neighbor[0], neighbor[1], dist + 1))
                seen.add(neighbor)

result = get_longest_path(new_graph, start, end)
print(result)
