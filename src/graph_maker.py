from pathlib import Path
from typing import Self
import random as rd
import networkx as nx
import pyvis.network as pn
import webbrowser as wb

class GraphMaker:
    __OUTPUT_PATH: Path = Path('graph.html').resolve()
    __edges: list[tuple[int, int]]
    __graph: nx.DiGraph
    __visual: pn.Network

    def __init__(self: Self, n: int) -> None:
        """
        Args:
            n: the number of edges and vertices in the graph to be made
        """
        self.__edges = []
        for i in range(n):
            while True:
                random_int = rd.randrange(n)
                if random_int != i: break # a person cannot choose themselves
            self.__edges.append((i, random_int))

    @property 
    def Edges(self: Self) -> list[tuple[int, int]]:
        return self.__edges
    
    @Edges.deleter
    def Edges(self: Self) -> None:
        del self.__edges

    @property
    def DiGraph(self: Self) -> nx.DiGraph:
        self.__graph = nx.DiGraph()
        self.__graph.add_edges_from(self.__edges)

        return self.__graph
    
    @DiGraph.deleter
    def DiGraph(self: Self) -> None:
        del self.__graph
    
    @property
    def Network(self: Self) -> pn.Network:
        self.__visual = pn.Network(directed=True)
        self.__visual.from_nx(self.DiGraph)

        for i in range(len(self.__visual.nodes)):
            self.__visual.nodes[i]['label'] = str(i)
        
        return self.__visual
    
    @Network.deleter
    def Network(self: Self) -> None:
        del self.__visual
    
    def show(self: Self) -> None:
        
        self.Network.write_html(str(self.__OUTPUT_PATH))
        wb.open('file://' + str(self.__OUTPUT_PATH))
        return
    
    def clear(self: Self) -> None:
        del self.Edges
        del self.DiGraph
        del self.Network
        return