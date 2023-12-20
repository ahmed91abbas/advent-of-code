with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]


class FlipFlop:
    def __init__(self, name):
        self.name = name
        self.on = False

    def handle_pulse(self, pulse):
        if pulse == 1:
            return
        if pulse == 0:
            if not self.on:
                self.on = True
                return 1
            else:
                self.on = False
                return 0

    def __repr__(self):
        return str(self.on)


class Conjunction:
    def __init__(self, name):
        self.name = name
        self.inputs = {}

    def add_input(self, name):
        self.inputs[name] = 0

    def handle_pulse(self, name, pulse):
        self.inputs[name] = pulse
        if all(self.inputs.values()):
            return 0
        else:
            return 1

    def __repr__(self):
        return str(self.inputs)


def button(connections, modules):
    lows = 1
    highs = 0
    # print("button -low-> broadcaster")
    pulses = [("broadcaster", x, 0) for x in connections["broadcaster"]]
    while pulses:
        sender, receiver, pulse = pulses.pop(0)
        # print(f"{sender} -{'high' if pulse else 'low'}-> {receiver}")
        if pulse == 0:
            lows += 1
        elif pulse == 1:
            highs += 1
        if not receiver in modules:
            continue
        if type(modules[receiver]) == FlipFlop:
            new_pulse = modules[receiver].handle_pulse(pulse)
            if new_pulse is not None:
                pulses.extend([(receiver, x, new_pulse) for x in connections[receiver]])
        elif type(modules[receiver]) == Conjunction:
            new_pulse = modules[receiver].handle_pulse(sender, pulse)
            pulses.extend([(receiver, x, new_pulse) for x in connections[receiver]])
    # print()
    return lows, highs


modules = {}
connections = {}
for line in lines:
    first, to = line.split(" -> ")
    name = first[1:]
    if first[0] == "%":
        modules[name] = FlipFlop(name)
    elif first[0] == "&":
        modules[name] = Conjunction(name)
    else:
        name = first
    connections[name] = to.split(", ")

for name, connection in connections.items():
    if name in modules:
        for c in connection:
            if c in modules and type(modules[c]) == Conjunction:
                modules[c].add_input(name)

total_lows = 0
total_highs = 0
for i in range(1000):
    lows, highs = button(connections, modules)
    total_lows += lows
    total_highs += highs

print(total_lows * total_highs)
