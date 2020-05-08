from functions.prims_functions import *
# from functions.drawings import *
from algo_prims import *

def prims(graph_path):
    G = read_graph(graph_path)
    starting = 'A'
    # starting = G.get_random_node()
    # print("Starting node is :", starting)

    T = minimum_spanning_tree(G, starting)

    for e in T.edges:
        print(e.nodes, " cost is ", e.cost)

prims("./data/G2.txt")