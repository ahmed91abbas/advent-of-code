from collections import defaultdict

with open("data.in") as f:
    lines = f.read().splitlines()

beams = defaultdict(int)
beams[lines[0].index("S")] = 1
for line in lines[1:]:
    current_beams = defaultdict(int)
    for b, num in beams.items():
        if line[b] == "^":
            if b - 1 >= 0:
                current_beams[b - 1] += num
            if b + 1 < len(line):
                current_beams[b + 1] += num
        else:
            current_beams[b] += num
    beams = current_beams

answer = sum(beams.values())
print(answer)
