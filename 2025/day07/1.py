with open("data.in") as f:
    lines = f.read().splitlines()

beams = set()
beams.add(lines[0].index("S"))
answer = 0
for line in lines[1:]:
    for b in beams.copy():
        if line[b] == "^":
            answer += 1
            beams.remove(b)
            if b - 1 >= 0:
                beams.add(b - 1)
            if b + 1 < len(line):
                beams.add(b + 1)
print(answer)
