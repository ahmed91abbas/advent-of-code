def is_safe(levels):
    first_cond = levels == sorted(levels) or levels == sorted(levels, reverse=True)
    if first_cond:
        diffs = sorted([abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)])
        second_cond = diffs[0] >= 1 and diffs[-1] <= 3
        print(first_cond, levels, second_cond)
    return first_cond and second_cond


with open("data.in") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    levels = list(map(int, line.split(" ")))
    ok = is_safe(levels)
    if ok:
        res += 1
        continue
    else:
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i + 1 :]
            ok = is_safe(new_levels)
            if ok:
                res += 1
                break
        if not ok:
            print(line)

print(res)
