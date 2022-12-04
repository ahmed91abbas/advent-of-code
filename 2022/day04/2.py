with open("data.in", "r") as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    a1, a2 = line.split(",")
    range1 = [int(x) for x in a1.split("-")]
    range2 = [int(x) for x in a2.split("-")]
    if (
        (range1[0] >= range2[0] and range1[0] <= range2[1])
        or (range1[1] >= range2[0] and range1[1] <= range2[1])
        or (range2[0] >= range1[0] and range2[0] <= range1[1])
        or (range2[1] >= range1[0] and range2[1] <= range1[1])
    ):
        result += 1

print(result)
