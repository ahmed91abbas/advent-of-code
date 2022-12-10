with open("data.in", "r") as f:
    lines = f.read().splitlines()

pic = ["." for _ in range(240)]

cycles = 0
x = 1
for line in lines:
    if line == "noop":
        if cycles % 40 in [x - 1, x, x + 1]:
            pic[cycles] = "#"
        cycles += 1
    else:
        if cycles % 40 in [x - 1, x, x + 1]:
            pic[cycles] = "#"
        cycles += 1
        if cycles % 40 in [x - 1, x, x + 1]:
            pic[cycles] = "#"
        cycles += 1
        x = x + int(line.split(" ")[1])

pic = "".join(pic)
for i in range(0, 240, 40):
    print(pic[i : i + 40])
