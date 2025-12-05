with open("data.in") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    batteries = []
    remaining = 12
    bank = [int(a) for a in line.strip()]
    while remaining > 0:
        current = max(bank[: len(bank) - remaining + 1])
        remaining -= 1
        bank = bank[bank.index(current) + 1 :]
        batteries.append(current)
    answer += int("".join(str(b) for b in batteries))
print(answer)
