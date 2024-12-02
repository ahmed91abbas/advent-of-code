with open("data.in") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    levels = list(map(int, line.split(" ")))
    first_cond = levels == sorted(levels) or levels == sorted(levels, reverse=True)
    if first_cond:
        diffs = sorted([abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)])
        second_cond = diffs[0] >= 1 and diffs[-1] <= 3
    if first_cond and second_cond:
        res += 1

print(res)
