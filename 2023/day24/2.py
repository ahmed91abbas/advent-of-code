import re

import z3


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


with open("data.in") as f:
    lines = f.readlines()

hailstones = []
for line in lines:
    x, y, z, vx, vy, vz = map(int, re.findall(r"[-\d]+", line))
    hailstones.append(Hailstone(x, y, z, vx, vy, vz))


solver = z3.Solver()
x, y, z, vx, vy, vz = z3.Ints("x y z vx vy vz")
for i, hs in enumerate(hailstones):
    t = z3.Int(f"t{i}")
    solver.add(x + vx * t == hs.x + hs.vx * t)
    solver.add(y + vy * t == hs.y + hs.vy * t)
    solver.add(z + vz * t == hs.z + hs.vz * t)
solver.check()
m = solver.model()
x, y, z = (m[v].as_long() for v in (x, y, z))
print(x + y + z)
