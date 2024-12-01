with open("data.in") as f:
    lines = f.read().splitlines()

left = []
right = []
for line in lines:
    l, r = line.split("   ")
    left.append(int(l))
    right.append(int(r))

pairs = list(zip(sorted(left), sorted(right)))
diff_sum = 0
for l, r in pairs:
    diff_sum += abs(l - r)

print(diff_sum)
