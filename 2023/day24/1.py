import re


class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __repr__(self):
        return str(self.__dict__)


def get_line_coefs(p1, p2):
    a = p1[1] - p2[1]
    b = p2[0] - p1[0]
    c = p1[0] * p2[1] - p2[0] * p1[1]
    return a, b, -c


def intersection(line1, line2):
    d = line1[0] * line2[1] - line1[1] * line2[0]
    dx = line1[2] * line2[1] - line1[1] * line2[2]
    dy = line1[0] * line2[2] - line1[2] * line2[0]
    if d != 0:
        x = dx / d
        y = dy / d
        return x, y
    else:
        return False


input = ("small.in", 7, 27)
input = ("data.in", 200000000000000, 400000000000000)
with open(input[0]) as f:
    lines = f.readlines()

hailstones = []
for line in lines:
    x, y, z, vx, vy, vz = map(int, re.findall(r"[-\d]+", line))
    hailstones.append(Hailstone(x, y, z, vx, vy, vz))

result = 0
min_value = input[1]
max_value = input[2]
for i, hs_a in enumerate(hailstones):
    for hs_b in hailstones[:i]:
        line1 = get_line_coefs([hs_a.x, hs_a.y], [hs_a.x + hs_a.vx, hs_a.y + hs_a.vy])
        line2 = get_line_coefs([hs_b.x, hs_b.y], [hs_b.x + hs_b.vx, hs_b.y + hs_b.vy])
        intersec = intersection(line1, line2)
        if not intersec:
            continue
        x, y = intersec
        if (
            min_value <= x <= max_value
            and min_value <= y <= max_value
            and ((x - hs_a.x) * hs_a.vx >= 0 and (y - hs_a.y) * hs_a.vy >= 0)
            and ((x - hs_b.x) * hs_b.vx >= 0 and (y - hs_b.y) * hs_b.vy >= 0)
        ):
            result += 1

print(result)
