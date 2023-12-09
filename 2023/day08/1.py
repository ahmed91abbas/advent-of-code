import re

with open("data.in", "r") as f:
    lines = f.readlines()


class Node:
    def __init__(self, name, L, R):
        self.name = name
        self.L = L
        self.R = R

    def get(self, direction):
        return self.L if direction == "L" else self.R

    def __repr__(self):
        return f"{self.name} -> {self.L}, {self.R}"


instructions = list(lines[0].strip())
nodes = {}
for line in lines[2:]:
    pattern = re.compile(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)")
    match = pattern.match(line)
    name, L, R = match.groups()
    nodes[name] = Node(name, L, R)

dest = None
steps = 0
index = 0
next_node = "AAA"
next_instruction = instructions[index]
while dest != "ZZZ":
    steps += 1
    dest = nodes[next_node].get(next_instruction)
    next_node = dest
    index = (index + 1) % len(instructions)
    next_instruction = instructions[index]
print(steps)
