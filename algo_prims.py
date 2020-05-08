from functions.prims_functions import *

def minimum_spanning_tree(G, start_node):
    T = Graph()

    # First minimum cost edge
    first_edges = get_all_edges(G, start_node)
    first_min_edge = minimum_cost_edge(first_edges)
    T.add_edge(first_min_edge)

    while len(T.get_nodes()) != len(G.get_nodes()):
        # List all edges from the tree connected to the tree
        edges_list = []
        for n in T.get_nodes():
            for e in get_all_edges(G, n):
                print(e.nodes)
                if not (e in T.edges and T.nodes_in_tree(e.nodes)):
                    edges_list.append(e)

        T.add_edge(minimum_cost_edge(edges_list))
        print(T.get_nodes())
    
    return T
