from copy import deepcopy

with open("data.in") as f:
    lines = f.read().splitlines()

guard_x, guard_y = (0, 0)
s_x, s_y = (0, 0)
for i, line in enumerate(lines):
    try:
        guard_x = line.index("^")
        guard_y = i
        s_x = guard_x
        s_y = guard_y
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

limit = len(steps) * 2

res = 0
for step in set(steps):
    new_lines = deepcopy(lines)
    if step == (s_x, s_y):
        continue
    new_string = new_lines[step[1]][: step[0]] + "#" + new_lines[step[1]][step[0] + 1 :]
    new_lines[step[1]] = new_string
    done = False
    steps = []
    dir_x = 0
    dir_y = -1
    cyclic = False
    guard_x = s_x
    guard_y = s_y
    while not done:
        x = guard_x + dir_x
        y = guard_y + dir_y
        if x >= len(new_lines[0]) or y >= len(new_lines) or x < 0 or y < 0:
            done = True
        elif len(steps) > limit:
            done = True
            cyclic = True
        elif new_lines[y][x] != "#":
            steps.append((x, y))
            guard_x = x
            guard_y = y
        else:
            dir_x, dir_y = directions[(dir_x, dir_y)]
    if cyclic:
        res += 1

print(res)
