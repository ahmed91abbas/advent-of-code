with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

plan = []
rows = 0
cols = 0
max_r = 0
max_d = 0
for line in lines:
    direction, distance, color = line.split(" ")
    distance = int(distance)
    plan.append((direction, distance, color))
    if direction == "R":
        cols += distance
        max_r = max(max_r, cols, distance)
    elif direction == "L":
        cols -= distance
        cols = abs(cols)
        max_r = max(max_r, cols, distance)
    elif direction == "U":
        rows -= distance
        rows = abs(rows)
        max_d = max(max_d, rows, distance)
    elif direction == "D":
        rows += distance
        max_d = max(max_d, rows, distance)

graph = [["." for _ in range((max_r + 1) * 2)] for _ in range((max_d + 1) * 2)]
rows = len(graph) // 2
cols = len(graph[0]) // 2
path = []
for direction, distance, _ in plan:
    if direction == "R":
        for i in range(distance):
            graph[rows][cols + i] = "#"
            path.append((rows, cols + i))
        cols += distance
    elif direction == "L":
        for i in range(distance):
            graph[rows][cols - i] = "#"
            path.append((rows, cols - i))
        cols -= distance
    elif direction == "U":
        for i in range(distance):
            graph[rows - i][cols] = "#"
            path.append((rows - i, cols))
        rows -= distance
    elif direction == "D":
        for i in range(distance):
            graph[rows + i][cols] = "#"
            path.append((rows + i, cols))
        rows += distance
    rows = abs(rows)
    cols = abs(cols)

result = 0
data = ""
for row in graph:
    try:
        start = row.index("#")
        end = len(row) - row[::-1].index("#") - 1
        result += end - start
    except ValueError:
        pass

area = 0
for i in range(len(path)):
    area += (path[i - 1][0] + path[i][0]) * (path[i - 1][1] - path[i][1])
inside = (abs(area) - len(path) + 2) // 2
print(inside + len(path))
