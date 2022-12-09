with open("data.in", "r") as f:
    lines = f.read().splitlines()


def is_touching(hx, hy, tx, ty):
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


def move_tail(hx, hy, tx, ty):
    # move right and left
    if hy == ty:
        if hx > tx:
            return tx + 1, ty
        elif hx < tx:
            return tx - 1, ty
    # move up and down
    if hx == tx:
        if hy > ty:
            return tx, ty + 1
        elif hy < ty:
            return tx, ty - 1
    # move diagonal up-right
    if hx > tx and hy > ty:
        return tx + 1, ty + 1
    # move diagonal up-left
    if hx < tx and hy > ty:
        return tx - 1, ty + 1
    # move diagonal down-right
    if hx > tx and hy < ty:
        return tx + 1, ty - 1
    # move diagonal down-left
    if hx < tx and hy < ty:
        return tx - 1, ty - 1


rope = [(0, 0) for _ in range(10)]
positions = {(0, 0)}
for line in lines:
    direction, steps = line.split(" ")
    steps = int(steps)
    for i in range(steps):
        hx, hy = rope[0]
        if direction == "R":
            hx += 1
        elif direction == "L":
            hx -= 1
        elif direction == "U":
            hy += 1
        elif direction == "D":
            hy -= 1
        rope[0] = (hx, hy)
        for i in range(1, len(rope)):
            x1, y1 = rope[i - 1]
            x2, y2 = rope[i]
            if not is_touching(x1, y1, x2, y2):
                new_x, new_y = move_tail(x1, y1, x2, y2)
                rope[i] = (new_x, new_y)
                if i == len(rope) - 1:
                    positions.add(rope[i])
print(len(positions))
