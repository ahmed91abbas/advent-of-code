class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def combine(self, r):
        s = r.start
        e = r.end
        if s >= self.start and s <= self.end:
            self.end = max(self.end, e)
            return True
        if s <= self.start and e >= self.start:
            self.start = s
            self.end = max(self.end, e)
            return True
        return False

    def __repr__(self):
        return f"{self.start}-{self.end}"


with open("data.in") as f:
    lines = f.read().splitlines()

fresh = []
for i, line in enumerate(lines):
    if "-" not in line:
        break
    parts = line.split("-")
    r = Range(int(parts[0]), int(parts[1]))
    for fr in fresh:
        if fr.combine(r):
            break
    else:
        fresh.append(r)

run = True
while run:
    current_len = len(fresh)
    for i in range(len(fresh)):
        for j in range(i + 1, len(fresh)):
            if fresh[i].combine(fresh[j]):
                del fresh[j]
                break
    if len(fresh) == current_len:
        run = False

answer = 0
for r in fresh:
    answer += r.end - r.start + 1
print(answer)
