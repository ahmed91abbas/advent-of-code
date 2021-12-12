from collections import deque


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
            if neighbor.isupper() or neighbor not in path:
                new_path = path.copy()
                new_path.append(neighbor)
                queue.append(new_path)
    return nbr_of_paths


with open('data.in') as f:
    lines = f.read().splitlines()

graph = {}
for line in lines:
    n1, n2 = line.split('-')
    if n1 not in graph:
        graph[n1] = [n2]
    else:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2] = [n1]
    else:
        graph[n2].append(n1)

print(get_nbr_of_paths(graph, 'start', 'end'))
