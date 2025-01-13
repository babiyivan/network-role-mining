import networkx as nx

# Read the GraphML file
# graph = nx.read_graphml('graphs/replies-253.graphml')
# graph = nx.read_graphml('graphs/votes-253.graphml')
graph = nx.read_graphml('graphs/follows-253.graphml')

# Create a mapping from node labels to integer IDs
label_to_id = {label: idx for idx, label in enumerate(graph.nodes())}

# Write the mapping to a file
# with open('graphs/labels-replies-253.txt', 'w') as f:
#     for label, idx in label_to_id.items():
#         f.write(f"{idx} {label}\n")
# with open('graphs/labels-votes-253.txt', 'w') as f:
#     for label, idx in label_to_id.items():
#         f.write(f"{idx} {label}\n")
with open('graphs/labels-follows-253.txt', 'w') as f:
    for label, idx in label_to_id.items():
        f.write(f"{idx} {label}\n")

# Write the edges to a file using the integer IDs
# with open('graphs/replies-253.edgelist', 'w') as f:
#     for edge in graph.edges():
#         f.write(f"{label_to_id[edge[0]]} {label_to_id[edge[1]]}\n")
# with open('graphs/votes-253.edgelist', 'w') as f:
#     for edge in graph.edges():
#         f.write(f"{label_to_id[edge[0]]} {label_to_id[edge[1]]}\n")
with open('graphs/follows-253.edgelist', 'w') as f:
    for edge in graph.edges():
        f.write(f"{label_to_id[edge[0]]} {label_to_id[edge[1]]}\n")