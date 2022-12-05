def print_diagram(diagram):
    for y in range(10):
        row = ""
        for x in range(10):
            key = str((x, y))
            if key in diagram:
                row += str(diagram[key])
            else:
                row += "."
        print(row)


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


def add_diagonal_left_to_right(diagram, s1, f1, s2, f2):
    while f1 >= s1 and f2 >= s2:
        key = str((f1, f2))
        if key in diagram:
            diagram[key] += 1
        else:
            diagram[key] = 1
        f1 -= 1
        f2 -= 1


def add_diagonal_right_to_left(diagram, s1, f1, s2, f2):
    while f1 >= s1 and f2 <= s2:
        key = str((f2, f1))
        if key in diagram:
            diagram[key] += 1
        else:
            diagram[key] = 1
        f1 -= 1
        f2 += 1


with open("data.in") as f:
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
    if abs(x1 - y1) == abs(x2 - y2):
        add_diagonal_left_to_right(diagram, x1, x2, y1, y2)
        add_diagonal_left_to_right(diagram, x2, x1, y2, y1)
    if abs(x1 - x2) == abs(y1 - y2):
        add_diagonal_right_to_left(diagram, y1, y2, x1, x2)
        add_diagonal_right_to_left(diagram, y2, y1, x2, x1)


# print_diagram(diagram)
print(len([x for x in diagram.values() if x > 1]))
