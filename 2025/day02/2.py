def get_invalid_ids(start, end):
    invalid_ids = []
    for i in range(start, end + 1):
        current = str(i)
        if current in (current + current)[1:-1]:
            invalid_ids.append(i)
    return invalid_ids


with open("data.in") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    ranges = line.split(",")
    for r in ranges:
        id1, id2 = map(int, r.split("-"))
        invalid_ids = get_invalid_ids(id1, id2)
        answer += sum(invalid_ids)

print(answer)
