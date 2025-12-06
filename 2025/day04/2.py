"""
-------> x
|
|
v
y
"""


class Node:
    def __init__(self, value, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.value = value

    def get_adjacent_indices(self):
        adjacent = []
        if self.x > 0:
            adjacent.append((self.x - 1, self.y))
        if self.x < self.max_x - 1:
            adjacent.append((self.x + 1, self.y))
        if self.y > 0:
            adjacent.append((self.x, self.y - 1))
        if self.y < self.max_y - 1:
            adjacent.append((self.x, self.y + 1))
        if self.x > 0 and self.y > 0:
            adjacent.append((self.x - 1, self.y - 1))
        if self.x < self.max_x - 1 and self.y > 0:
            adjacent.append((self.x + 1, self.y - 1))
        if self.x > 0 and self.y < self.max_y - 1:
            adjacent.append((self.x - 1, self.y + 1))
        if self.x < self.max_x - 1 and self.y < self.max_y - 1:
            adjacent.append((self.x + 1, self.y + 1))
        return adjacent

    def __repr__(self):
        return f"({self.x}, {self.y}): {self.value}"


def solve(current_graph):
    valid = []
    prow = ""
    for row in current_graph:
        for node in row:
            adjacent_papers = 0
            for indices in node.get_adjacent_indices():
                adjacent_node = current_graph[indices[1]][indices[0]]
                if adjacent_node.value == "@":
                    adjacent_papers += 1
            if adjacent_papers < 4 and node.value == "@":
                valid.append(node)
                prow += "X"
            else:
                prow += node.value
        prow += "\n"
    # print(prow)
    # print("\n")
    return valid, current_graph


with open("data.in") as f:
    lines = f.read().splitlines()

gragh = []
for y, line in enumerate(lines):
    row = []
    for x, char in enumerate(line.strip()):
        row.append(Node(char, x, y, len(line.strip()), len(lines)))
    gragh.append(row)

answer = 0
while True:
    valid, gragh = solve(gragh)
    if len(valid) == 0:
        break
    answer += len(valid)
    for node in valid:
        gragh[node.y][node.x].value = "."

print(answer)
