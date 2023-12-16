with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


"""
---1>-------2<--------> x
|
3
v
|
|
4
n
|
|
v
y

1 = (1, 0)
2 = (-1, 0)
3 = (0, 1)
4 = (0, -1)
"""


class Beam:
    def __init__(self, x, y, max_x, max_y, dir):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.dir = dir

    def move(self):
        self.x += self.dir[0]
        self.y += self.dir[1]

    def split(self, tile):
        if tile == ".":
            return self, None
        if tile == "|":
            if self.dir[0] == 0:
                return self, None
            if self.dir[1] == 0:
                self.dir = (0, 1)
                return self, Beam(self.x, self.y, self.max_x, self.max_y, (0, -1))
        if tile == "-":
            if self.dir[0] == 0:
                self.dir = (1, 0)
                return self, Beam(self.x, self.y, self.max_x, self.max_y, (-1, 0))
            if self.dir[1] == 0:
                return self, None
        if tile == "/":
            if self.dir == (1, 0):
                self.dir = (0, -1)
                return self, None
            if self.dir == (-1, 0):
                self.dir = (0, 1)
                return self, None
            if self.dir == (0, 1):
                self.dir = (-1, 0)
                return self, None
            if self.dir == (0, -1):
                self.dir = (1, 0)
                return self, None
        if tile == "\\":
            if self.dir == (1, 0):
                self.dir = (0, 1)
                return self, None
            if self.dir == (-1, 0):
                self.dir = (0, -1)
                return self, None
            if self.dir == (0, 1):
                self.dir = (1, 0)
                return self, None
            if self.dir == (0, -1):
                self.dir = (-1, 0)
                return self, None

    def finished(self):
        return self.x < 0 or self.y < 0 or self.x >= self.max_x or self.y >= self.max_y

    @property
    def key(self):
        return f"{self.x}, {self.y}, {self.dir}"


def get_energy(graph, entry_point):
    start_beam = Beam(entry_point[0], entry_point[1], len(graph[0]), len(graph), entry_point[2])
    beams = {start_beam}
    energized = set()
    handled = set()
    while beams:
        current_beam = beams.pop()
        while not current_beam.finished() and current_beam.key not in handled:
            energized.add((current_beam.x, current_beam.y))
            handled.add(current_beam.key)
            tile = graph[current_beam.y][current_beam.x]
            current_beam, new_beam = current_beam.split(tile)
            if new_beam:
                beams.add(new_beam)
            current_beam.move()
    return len(energized)


graph = []
for line in lines:
    graph.append(list(line))


entry_points = []
for y in range(len(graph)):
    entry_points.append((0, y, (1, 0)))
    entry_points.append((len(graph[0]) - 1, y, (-1, 0)))
for x in range(len(graph[0])):
    entry_points.append((x, 0, (0, 1)))
    entry_points.append((x, len(graph) - 1, (0, -1)))

max_energy = 0
for entry_point in entry_points:
    energy = get_energy(graph, entry_point)
    if energy > max_energy:
        max_energy = energy
print(max_energy)
