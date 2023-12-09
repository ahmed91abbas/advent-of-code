import re
import math

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
a_nodes = set()
z_nodes = set()
for line in lines[2:]:
    pattern = re.compile(r"(\w+)\s*=\s*\((\w+),\s*(\w+)\)")
    match = pattern.match(line)
    name, L, R = match.groups()
    nodes[name] = Node(name, L, R)
    if name[2] == "A":
        a_nodes.add(name)
    elif name[2] == "Z":
        z_nodes.add(name)

result = []
for node in a_nodes:
    steps = 0
    index = 0
    dest = None
    while dest not in z_nodes:
        steps += 1
        dest = nodes[node].get(instructions[index])
        node = dest
        index = (index + 1) % len(instructions)
    result.append(steps)
print(math.lcm(*result))
