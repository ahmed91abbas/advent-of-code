from collections import defaultdict
from heapq import heappop as pop
from heapq import heappush as push

with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

graph = [list(map(int, line)) for line in lines]
rows, cols = len(graph), len(graph[0])


costs = defaultdict(lambda: float("inf"))
costs[(0, 0, 0, 1, 0)] = 0
costs[(0, 0, 1, 0, 0)] = 0
# i, j, di, dj, steps
queue = [(0, 0, 0, 1, 0), (0, 0, 1, 0, 0)]
result = float("inf")
while queue:
    i, j, di, dj, steps = pop(queue)
    cost = costs[(i, j, di, dj, steps)]
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if i == rows - 1 and j == cols - 1 and steps >= 4:
        result = min(result, cost)
        continue
    for mi, mj in moves:
        if di == -mi and dj == -mj:
            continue
        ni = i + mi
        nj = j + mj
        if 0 <= ni < rows and 0 <= nj < cols:
            new_cost = cost + graph[ni][nj]
            same_dir = di == mi and dj == mj
            new_steps = steps + 1 if same_dir else 1
            if ((new_steps <= 10 and same_dir) or (steps >= 4 and not same_dir)) and new_cost < costs[
                (ni, nj, mi, mj, new_steps)
            ]:
                costs[(ni, nj, mi, mj, new_steps)] = new_cost
                push(queue, (ni, nj, mi, mj, new_steps))

print(result)
