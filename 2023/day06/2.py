with open("data.in", "r") as f:
    lines = f.read().splitlines()


time = int(lines[0].replace("Time:", "").replace(" ", ""))
record = int(lines[1].replace("Distance:", "").replace(" ", ""))

better = 0
for hold in range(1, time):
    time_left = time - hold
    distance = time_left * hold
    if distance > record:
        better += 1

print(better)
