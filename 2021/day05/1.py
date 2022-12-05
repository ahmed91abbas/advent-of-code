def add_overlaps(diagram, start, finish, x=None, y=None):
    while finish >= start:
        if x:
            key = str((x, finish))
        else:
            key = str((finish, y))
        if key in diagram:
            diagram[key] += 1
        else:
            diagram[key] = 1
        finish -= 1


with open("small.in") as f:
    lines = f.read().splitlines()

diagram = dict()
for line in lines:
    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))
    if y1 == y2:
        add_overlaps(diagram, x1, x2, y=y1)
        add_overlaps(diagram, x2, x1, y=y1)
    if x1 == x2:
        add_overlaps(diagram, y1, y2, x=x1)
        add_overlaps(diagram, y2, y1, x=x1)

print(len([x for x in diagram.values() if x > 1]))
