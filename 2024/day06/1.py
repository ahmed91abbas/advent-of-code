with open("data.in") as f:
    lines = f.read().splitlines()

guard_x, guard_y = (0, 0)
for i, line in enumerate(lines):
    try:
        guard_x = line.index("^")
        guard_y = i
        break
    except:
        pass

directions = {
    (-1, 0): (0, -1),
    (0, 1): (-1, 0),
    (1, 0): (0, 1),
    (0, -1): (1, 0),
}

done = False
steps = []
dir_x = 0
dir_y = -1
while not done:
    x = guard_x + dir_x
    y = guard_y + dir_y
    if x >= len(lines[0]) or y >= len(lines) or x < 0 or y < 0:
        done = True
    elif lines[y][x] != "#":
        steps.append((x, y))
        guard_x = x
        guard_y = y
    else:
        dir_x, dir_y = directions[(dir_x, dir_y)]

print(len(set(steps)))
