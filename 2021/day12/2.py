from collections import deque


def is_visited(node, path):
    small_caves = [x for x in path if x.islower()]
    unique_small_caves = set(small_caves)
    if (
        node.isupper()
        or node not in path
        or (len(small_caves) == len(unique_small_caves) and node not in ["start", "end"])
    ):
        return False
    return True


def get_nbr_of_paths(graph, start, end):
    nbr_of_paths = 0
    queue = deque()
    queue.append([start])
    while queue:
        path = queue.popleft()
        last = path[len(path) - 1]
        if last == end:
            nbr_of_paths += 1
            # print(','.join(path))
        for neighbor in graph[last]:
            if not is_visited(neighbor, path):
                new_path = path.copy()
                new_path.append(neighbor)
                queue.append(new_path)
    return nbr_of_paths


with open("data.in") as f:
    lines = f.read().splitlines()

graph = {}
for line in lines:
    n1, n2 = line.split("-")
    if n1 not in graph:
        graph[n1] = [n2]
    else:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2] = [n1]
    else:
        graph[n2].append(n1)

print(get_nbr_of_paths(graph, "start", "end"))
