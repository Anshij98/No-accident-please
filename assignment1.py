import networkx as nx
import matplotlib.pyplot as plt

# Define the flight paths
flights = {
    'Flight 1': [(1, 1), (2, 2), (3, 3)],
    'Flight 2': [(1, 1), (2, 4), (3, 2)],
    'Flight 3': [(1, 1), (4, 2), (3, 4)]
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes for each airport
for flight, path in flights.items():
    for i, (x, y) in enumerate(path):
        G.add_node((x, y))

# Add edges for each flight
for flight, path in flights.items():
    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

# Use the spring layout algorithm to position the nodes
pos = nx.spring_layout(G)

# Draw the graph
nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray')

# Add labels for each flight
for flight, path in flights.items():
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(path[i], path[i + 1]): flight for i in range(len(path) - 1)})

plt.show()