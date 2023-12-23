from collections import defaultdict

with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

R = len(lines)
C = len(lines[0])
start = None
graph = {}
for i in range(R):
    for j in range(C):
        graph[(i, j)] = lines[i][j]
        if lines[i][j] == "S":
            start = (i, j)


def get_plots_per_steps(steps):
    current_plots = {start}
    plots = defaultdict(int)
    for i in range(1, steps + 1):
        new_plots = set()
        for plot in current_plots:
            x, y = plot
            for x, y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if graph[(x % R, y % C)] != "#":
                    new_plots.add((x, y))
        current_plots = new_plots
        plots[i] += len(new_plots)
    return plots


# Quadratic interpolation
steps = 26501365
x0 = start[0]
x1 = R + start[0]
x2 = 2 * R + start[0]
plots = get_plots_per_steps(x2)
y0 = plots[x0]
y1 = plots[x1]
y2 = plots[x2]
l0 = ((steps - x1) * (steps - x2)) / ((x0 - x1) * (x0 - x2))
l1 = ((steps - x0) * (steps - x2)) / ((x1 - x0) * (x1 - x2))
l2 = ((steps - x0) * (steps - x1)) / ((x2 - x0) * (x2 - x1))
y = y0 * l0 + y1 * l1 + y2 * l2
print(round(y))
