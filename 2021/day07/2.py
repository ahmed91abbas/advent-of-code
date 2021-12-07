with open('data.in') as f:
    lines = f.read().splitlines()

positions = list(map(int, lines[0].split(',')))
min_cost = None
res_pos = 0
for i in range(max(positions) + 1):
    current_cost = 0
    for pos in positions:
        n = abs(pos - i)
        current_cost += (n*(n+1))//2
    if min_cost == None or current_cost < min_cost:
        min_cost = current_cost
        res_pos = i

print('res_pos', res_pos, 'fuel', min_cost)
