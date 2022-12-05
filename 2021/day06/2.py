with open("data.in") as f:
    lines = f.read().splitlines()

life_cycle = [0] * 9
for fish in lines[0].split(","):
    life_cycle[int(fish)] += 1

days = 256
for day in range(1, days + 1):
    grown_up_fish = life_cycle.pop(0)
    life_cycle[6] += grown_up_fish
    life_cycle.append(grown_up_fish)
    # print(f'day {day}: {sum(life_cycle)}')

print(sum(life_cycle))
