from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

with open("data.in", "r") as f:
    lines = [line.strip() for line in f.readlines()]

graph = defaultdict(set)
for line in lines:
    key, value = line.split(":")
    for m in value.split(" "):
        if m:
            graph[key].add(m)
            graph[m].add(key)

G = nx.Graph(graph)


def draw():
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    plt.show()


# draw()
G.remove_edges_from(nx.minimum_edge_cut(G))
# draw()

connected_components = list(nx.connected_components(G))
print(len(connected_components[0]) * len(connected_components[1]))
