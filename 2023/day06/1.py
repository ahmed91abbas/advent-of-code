import re
import math

with open("data.in", "r") as f:
    lines = f.read().splitlines()

times = list(map(int, re.findall(r"\d+", lines[0])))
records = list(map(int, re.findall(r"\d+", lines[1])))

best = []
for i in range(len(times)):
    better = []
    for time in range(1, times[i]):
        time_left = times[i] - time
        distance = time_left * time
        if distance > records[i]:
            better.append(i)
    best.append(len(better))

print(math.prod(best))
