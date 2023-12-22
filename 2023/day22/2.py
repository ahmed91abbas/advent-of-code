import functools

with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2

    def overlaps(self, other):
        return max(self.x1, other.x1) < min(self.x2, other.x2) and max(self.y1, other.y1) < min(self.y2, other.y2)

    def is_supporting(self, other):
        return self.z2 == other.z1 and self.overlaps(other)

    def __repr__(self):
        return f"({self.x1}..{self.x2}, {self.y1}..{self.y2}, {self.z1}..{self.z2})"


def fall(index):
    current = bricks[index]
    valid_z = [0]
    for i in range(len(bricks)):
        if index == i:
            continue
        if current.overlaps(bricks[i]) and bricks[i].z2 <= current.z1:
            valid_z.append(bricks[i].z2)
    delta = max(valid_z) - current.z1
    current.z1 += delta
    current.z2 += delta
    bricks[index] = current


@functools.cache
def get_supported_by(index):
    return [i for i in range(len(bricks)) if i != index and bricks[index].is_supporting(bricks[i])]


@functools.cache
def get_supporting(index):
    return [i for i in range(len(bricks)) if i != index and bricks[i].is_supporting(bricks[index])]


def disintegrate(index):
    queue = [index]
    would_fall = {index}
    while queue:
        current = queue.pop(0)
        for s in get_supported_by(current):
            if all(x in would_fall for x in get_supporting(s)) and s not in would_fall:
                would_fall.add(s)
                queue.append(s)
    return would_fall


bricks = []
for line in lines:
    p1, p2 = line.split("~")
    x1, y1, z1 = [int(i) for i in p1.split(",")]
    x2, y2, z2 = [int(i) for i in p2.split(",")]
    bricks.append(Brick(x1, y1, z1, x2 + 1, y2 + 1, z2 + 1))

bricks = sorted(bricks, key=lambda b: b.z1)

for i in range(len(bricks)):
    fall(i)

result = 0
for i in range(len(bricks)):
    disintegrated = disintegrate(i)
    result += len(disintegrated) - 1
print(result)
