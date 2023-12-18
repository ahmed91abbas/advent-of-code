with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

dir_map = {
    "0": (1, 0),
    "1": (0, 1),
    "2": (-1, 0),
    "3": (0, -1),
}

plan = []
for line in lines:
    _, _, color = line.split(" ")
    direction = dir_map[color[-2:-1]]
    distance = int(color[2:-2], 16)
    plan.append((direction, distance))

direction, distance = plan[0]
edges = [(distance * direction[0], distance * direction[1])]
for direction, distance in plan[1:]:
    current = edges[-1]
    next_point = (current[0] + distance * direction[0], current[1] + distance * direction[1])
    edges.append(next_point)

areas = []
# cross product
for i in range(len(edges) - 2):
    areas.append(edges[i][0] * edges[i + 1][1] - edges[i][1] * edges[i + 1][0])

result = (sum(areas) + sum(distance for _, distance in plan)) // 2 + 1
print(result)
