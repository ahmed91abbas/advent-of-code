with open("data.in") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    a = -1
    b = -1
    bank = line.strip()
    for i, c in enumerate(bank):
        c = int(c)
        if c > a and i < len(bank) - 1:
            a = c
            b = -1
        elif c >= b:
            b = c
    # print(line, int(str(a) + str(b)))
    answer += int(str(a) + str(b))
print(answer)
