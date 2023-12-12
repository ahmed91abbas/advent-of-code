import functools

with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def get_combinations(data, groups):
    @functools.cache
    def _get_combinations(data_index, group_index):
        if group_index == len(groups):
            return 1 if "#" not in data[data_index:] else 0

        combinations = 0
        for i in range(data_index, len(data)):
            current = data[i : i + groups[group_index]]
            if (
                len(current) == groups[group_index]
                and "." not in current
                and (len(data) <= i + groups[group_index] or data[i + groups[group_index]] != "#")
            ):
                combinations += _get_combinations(i + groups[group_index] + 1, group_index + 1)
            if data[i] == "#":
                break

        return combinations

    return _get_combinations(0, 0)


result = 0
for line in lines:
    p1, p2 = line.split(" ")
    data = list("?".join(5 * [p1]))
    groups = [int(x) for x in ",".join(5 * [p2]).split(",")]
    result += get_combinations(data, groups)

print(result)
