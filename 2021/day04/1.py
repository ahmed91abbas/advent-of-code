def get_flipped_grid(grid):
    result = list()
    for i in range(len(grid[0])):
        flipped = list()
        for row in grid:
            flipped.append(row[i])
        result.append(flipped)
    return result


def get_bingo(grids, numbers):
    marked = list()
    for n in numbers:
        marked.append(n)
        for grid in grids:
            for rc in grid:
                if all(x in marked for x in rc):
                    return n, marked, grid


with open("data.in") as f:
    lines = f.read().splitlines()

numbers = lines[0].split(",")
filtered_lines = [[x for x in line.split(" ") if x] for line in lines[1:] if line]
grids = list()
for i in range(0, len(filtered_lines), 5):
    grid = filtered_lines[i : i + 5]
    grid += get_flipped_grid(grid)
    grids.append(grid)

bingo, marked, grid = get_bingo(grids, numbers)

sum_unmarked = 0
for r in grid[: len(grid) // 2]:
    sum_unmarked += sum([int(x) for x in r if x not in marked])

print(sum_unmarked * int(bingo))
