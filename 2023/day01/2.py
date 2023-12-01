with open("data.in") as f:
    lines = f.read().splitlines()

word_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum = 0
for line in lines:
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        for word, digit in word_map.items():
            if line[i:].startswith(word):
                digits.append(digit)
                break
    sum += int(digits[0] + digits[-1])
print(sum)
