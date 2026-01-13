from pathlib import Path
from typing import Self
import random as rd
import networkx as nx
import pyvis.network as pn
import webbrowser as wb

class GraphMaker:
    __edges: list[tuple[int, int]] = []

    def __init__(self: Self, n: int) -> None:
        """
        Args:
            n: the number of edges and vertices in the graph to be made
        """
        for i in range(n):
            while True:
                random_int = rd.randrange(n)
                if random_int != i: break # a person cannot choose themselves
            self.__edges.append((i, random_int))

    @property
    def DiGraph(self: Self) -> nx.DiGraph:
        G: nx.DiGraph

        G = nx.DiGraph()
        G.add_edges_from(self.__edges)

        return G
    
    @property
    def Network(self: Self) -> pn.Network:
        N: pn.Network

        N = pn.Network(directed=True)
        N.from_nx(self.DiGraph)
        
        return N
    
    def show(self: Self) -> None:
        OUTPUT_PATH: str = str(Path('graph.html').resolve())
        
        self.Network.write_html(OUTPUT_PATH)
        wb.open("file://" + OUTPUT_PATH)

        return