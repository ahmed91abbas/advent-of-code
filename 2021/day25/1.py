def move(pos_list, busy_pos, max_count, dir):
    changed = False
    move_pairs = list()
    new_pos_list = list()
    for pos in pos_list:
        if dir == "south":
            next_pos = ((pos[0] + 1) % max_count, pos[1])
        else:
            next_pos = (pos[0], (pos[1] + 1) % max_count)
        if not busy_pos[next_pos]:
            move_pairs.append((pos, next_pos))
            new_pos_list.append(next_pos)
            changed = True
        else:
            new_pos_list.append(pos)
    for old, new in move_pairs:
        busy_pos[old] = False
        busy_pos[new] = True
    return new_pos_list, busy_pos, changed


with open("data.in") as f:
    lines = f.read().splitlines()

busy_pos = dict()
east_list = list()
south_list = list()
col_count = len(lines[0])
row_count = len(lines)
for i, line in enumerate(lines):
    for j, e in enumerate(line):
        current = lines[i][j]
        key = (i, j)
        busy_pos[key] = current != "."
        if current == ">":
            east_list.append(key)
        elif current == "v":
            south_list.append(key)


steps = 0
while True:
    steps += 1
    east_list, busy_pos, east_changed = move(east_list, busy_pos, col_count, "east")
    south_list, busy_pos, south_changed = move(south_list, busy_pos, row_count, "south")
    if not east_changed and not south_changed:
        break
print(steps)
