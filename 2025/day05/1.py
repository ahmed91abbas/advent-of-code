with open("data.in") as f:
    lines = f.read().splitlines()

fresh = []
for i, line in enumerate(lines):
    if "-" not in line:
        break
    parts = line.split("-")
    fresh.append((int(parts[0]), int(parts[1])))

answer = 0
for line in lines[i + 1 :]:
    num = int(line)
    for fr in fresh:
        if num >= fr[0] and num <= fr[1]:
            answer += 1
            break
print(answer)
