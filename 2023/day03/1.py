import re


class Hit:
    def __init__(self, number, start, end, row):
        self.number = number
        self.start = start
        self.end = end
        self.row = row

    def __repr__(self):
        return f"number({self.number}, {self.start}, {self.end}, {self.row})"

class Symbol:
    def __init__(self, symbol, row, column):
        self.symbol = symbol
        self.row = row
        self.column = column

    def __repr__(self):
        return f"symbol({self.symbol}, {self.row}, {self.column})"

with open("data.in") as f:
    lines = f.read().splitlines()

numbers = []
symbols = []
for i, line in enumerate(lines):
    numbers_match = re.finditer(r'\d+', line)
    symbols_match = re.finditer(r'[^.\d]+', line)
    numbers += [Hit(int(match.group()), match.start(), match.end() - 1, i) for match in numbers_match]
    symbols += [Symbol(match.group(), i, match.start()) for match in symbols_match]

valid_numbers = []
for number in numbers:
    for symbol in symbols:
        if number.row in range(symbol.row - 1, symbol.row + 2) and (number.start in range(symbol.column - 1, symbol.column + 2) or number.end in range(symbol.column - 1, symbol.column + 2)):
            valid_numbers.append(number.number)
            break

print(sum(valid_numbers))
