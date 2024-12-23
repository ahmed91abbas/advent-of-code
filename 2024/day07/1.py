def is_valid(expected, numbers):
    routes = [numbers.pop(0)]
    while numbers:
        current = numbers.pop(0)
        new_routes = []
        for n in routes:
            p = current + n
            m = current * n
            if p <= expected:
                new_routes.append(p)
            if m <= expected:
                new_routes.append(m)
        routes = new_routes
    return expected in new_routes


with open("data.in") as f:
    lines = f.read().splitlines()

valid = []
for line in lines:
    p1, p2 = line.split(":")
    expected = int(p1)
    numbers = [int(x) for x in p2.split(" ") if x]
    if is_valid(expected, numbers):
        valid.append(expected)

print(sum(valid))
