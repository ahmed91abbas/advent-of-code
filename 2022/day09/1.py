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


hx = 0
hy = 0
tx = 0
ty = 0
positions = {(tx, ty)}
for line in lines:
    direction, steps = line.split(" ")
    steps = int(steps)
    for i in range(steps):
        if direction == "R":
            hx += 1
        elif direction == "L":
            hx -= 1
        elif direction == "U":
            hy += 1
        elif direction == "D":
            hy -= 1
        if not is_touching(hx, hy, tx, ty):
            tx, ty = move_tail(hx, hy, tx, ty)
            positions.add((tx, ty))
print(len(positions))
