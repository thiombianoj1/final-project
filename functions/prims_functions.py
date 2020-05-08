from operator import attrgetter
import random


class Graph:
    """Class defining a graph"""
    def __init__(self):
        self.edges = []

    def add_edge(self, e):
        if e not in self.edges:
            self.edges.append(e)
    

    def nodes_in_tree(self, nodes):
        t_nodes = self.get_nodes()
        if (nodes[0] in t_nodes) and (nodes[1] in t_nodes):
            return True
        else:
            return False

    def compute_total_weight(self):
        total_weight = 0
        for e in self.edges:
            total_weight = total_weight + e.cost
        return total_weight

    def get_nodes(self):
        l = [i.nodes for i in self.edges]
        all_nodes = ()
        for t in l:
            all_nodes = all_nodes + t
        return sorted(list(set(all_nodes)))

    def get_random_node(self):
        if self.edges == []:
            return None
        else:
            return random.choice(self.get_nodes())


class Edge:
    """"Class defining an edge"""

    def __init(self, e):
        self.nodes = e.nodes
        self.cost = e.cost

    def __init__(self, line):
        self.cost = int(line.split(":")[1])
        txt_nodes = line.split(":")[0]
        self.nodes = (txt_nodes.split("-")[0], txt_nodes.split("-")[1])
    
    def __eq__(self, e):
        return (e.nodes == self.nodes) or (e.nodes[::-1] == self.nodes)


def read_graph(graph_path):
    """From a txt file, create a weighted graph object"""
    G = Graph()

    f = open(graph_path, "r")
    if f.mode == "r":
        for line in f.readlines():
            G.add_edge(Edge(line))
        return G
    else:
        print("Graph file not openned")


def get_all_edges(G, node):
    """Returns a list of all edges connected to a single node in the graph"""
    node_edges = []

    for e in G.edges:
        if node in e.nodes:
            node_edges.append(e)

    return node_edges


def minimum_cost_edge(edge_list):
    """From a list of weighted edges connected to a single node,
    returns the edge with the minimum cost"""
    return min(edge_list, key=attrgetter('cost'))
