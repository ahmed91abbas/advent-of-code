with open("data.in") as f:
    lines = f.read().splitlines()

left = []
right = []
for line in lines:
    l, r = line.split("   ")
    left.append(int(l))
    right.append(int(r))

sim_sum = 0
for x in left:
    sim_sum += x * right.count(x)

print(sim_sum)
