with open("data.in") as f:
    lines = f.read()


def parse_map(txt):
    return [[int(x) for x in line.split(" ")] for line in txt.split("\n")[1:]]


def get_next_ranges(ranges, map_to_handle):
    next_ranges = []
    for item in ranges:
        current = item[0]
        while current < item[1]:
            current_map = next((item for item in map_to_handle if item[1] <= current < item[1] + item[2]), None)
            if current_map:
                upper_bound = min(item[1] - current_map[1] + current_map[0], current_map[0] + current_map[2] - 1)
                next_item = (current - current_map[1] + current_map[0], upper_bound)
                next_ranges.append(next_item)
                current = min(item[1] + 1, current + next_item[1] - next_item[0] + 1)
            else:
                next_map = next(
                    (item for item in map_to_handle if current < item[1] and current + item[2] >= item[1]), None
                )
                if next_map:
                    next_ranges.append((current, next_map[1]))
                    current = next_map[1]
                else:
                    next_ranges.append((current, item[1]))
                    current = item[1] + 1
    return next_ranges


chunks = lines.split("\n\n")
seed_ranges = [int(x) for x in chunks[0].split(" ") if x.isdigit()]
seed_ranges = [(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)]

next_ranges = seed_ranges
for chunk in chunks[1:]:
    next_ranges = get_next_ranges(next_ranges, parse_map(chunk.strip()))

print(min([x[0] for x in next_ranges]))
