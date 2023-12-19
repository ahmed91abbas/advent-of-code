import math
import re
from collections import defaultdict

with open("data.in", "r") as f:
    lines = f.read()


class Edge:
    def __init__(self, node, condition):
        self.node = node
        self.condition = condition
        self.handled = False

    def __repr__(self):
        return f"{self.condition}:{self.node}"


def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for edge in graph[start]:
        node = edge.node
        if node not in path:
            new_paths = dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


chunks = lines.split("\n\n")
workflows = {}
for line in chunks[0].splitlines():
    pattern = r"(\w+)\{(.*)\}"
    match = re.match(pattern, line)
    name, workflow = match.groups()
    workflow = workflow.split(",")
    workflows[name] = workflow

graph = defaultdict(list)
for key, workflow in workflows.items():
    for rule in workflow:
        if ":" not in rule:
            graph[key].append(Edge(rule, None))
            continue
        condition, next_key = rule.split(":")
        pattern = r"(\w+)([<>])(\d+)"
        match = re.match(pattern, condition)
        name, operator, value = match.groups()
        value = int(value)
        graph[key].append(Edge(next_key, (name, operator, value)))


paths = dfs(graph, "in", "A")
min_range = 1
max_range = 4000
result = 0
for path in paths:
    values = {
        "x": (min_range, max_range),
        "m": (min_range, max_range),
        "a": (min_range, max_range),
        "s": (min_range, max_range),
    }
    for i in range(len(path) - 1):
        for edge in graph[path[i]]:
            handled = edge.handled
            edge.handled = True
            if edge.condition:
                name, operator, value = edge.condition
                if edge.node == path[i + 1] and not (handled and edge.node == "A"):
                    if operator == "<":
                        values[name] = (values[name][0], value - 1)
                    elif operator == ">":
                        values[name] = (value + 1, values[name][1])
                    break
                if operator == "<":
                    values[name] = (value, values[name][1])
                elif operator == ">":
                    values[name] = (values[name][0], value)
    result += math.prod([max(0, value[1] - value[0] + 1) for value in values.values()])

print(result)
