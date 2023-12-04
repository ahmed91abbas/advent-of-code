with open("data.in") as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    parts = line.split(":")
    game_id = parts[0].strip()
    cards = parts[1].split("|")
    winnings_numbers = [int(x) for x in cards[0].strip().split()]
    my_numbers = [int(x) for x in cards[1].strip().split()]
    count = 0
    for number in my_numbers:
        if number in winnings_numbers:
            if count:
                count *= 2
            else:
                count += 1
    result += count

print(result)
