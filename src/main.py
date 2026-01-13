from random import randrange
from pyvis.network import Network
import networkx as nx
import webbrowser
import os

n: int
edges: list[tuple[int, int]]
random_int: int
G: nx.DiGraph

n = 10 # if n < 2 or n not int: ask for number again
edges = []
for i in range(n):
    while True:
        random_int = randrange(0, n)
        if random_int != i: break # a person cannot choose themselves
    edges.append((i, random_int))

G = nx.DiGraph()
G.add_edges_from(edges)

net = Network(
    directed=True,
    height="750px",
    width="100%",
    bgcolor="#ffffff",
    font_color=True
)
net.from_nx(G)
output_file = "graph.html"
net.write_html(output_file)
webbrowser.open("file://" + os.path.abspath(output_file))