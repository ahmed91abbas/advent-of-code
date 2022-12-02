with open("data.in", "r") as f:
    lines = f.read().splitlines()

beats = {"A": "Y", "B": "Z", "C": "X"}
loses = {"A": "Z", "B": "X", "C": "Y"}
draws = {"A": "X", "B": "Y", "C": "Z"}
scores = {"X": 1, "Y": 2, "Z": 3}
result = 0
for line in lines:
    first, second = line.split()
    if second == "X":
        result += 0 + scores[loses[first]]
    elif second == "Y":
        result += 3 + scores[draws[first]]
    elif second == "Z":
        result += 6 + scores[beats[first]]

print(result)
