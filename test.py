from functions.prims_functions import *


G_1 = read_graph("./data/G2.txt")
G_2 = Graph()

for e in G_1.edges:
    print(e.nodes, " cost is ", e.cost)

print("")

for i in G_2.edges:
    print(i.nodes, " cost is ", i.cost)

print("")
print("All edges")
all_edges = get_all_edges(G_1, 'A')
for t in all_edges:
    print(t.nodes, " cost is ", t.cost)