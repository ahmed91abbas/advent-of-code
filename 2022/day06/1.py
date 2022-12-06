with open("data.in", "r") as f:
    buffer = f.read().splitlines()[0]

for i in range(len(buffer)):
    marker_len = 4
    marker = len(set(buffer[i : i + marker_len]))
    if marker == marker_len:
        print(i + marker_len)
        break
