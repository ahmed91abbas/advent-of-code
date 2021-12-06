with open('data.in') as f:
    lines = f.read().splitlines()

fish = list(map(int, lines[0].split(',')))
days = 80
for day in range(1, days+1):
    next_gen = []
    for i in range(len(fish)):
        if fish[i] == 0:
            next_gen += [8]
            fish[i] = 6
        else:
            fish[i] -= 1
    fish += next_gen
    # print(f'day {day}: {fish}')

print(len(fish))
