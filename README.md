Here we  use a graph-based approach to find the shortest path for each flight while avoiding intersections. Here's a step-by-step explanation:

Step 1: Create a graph
Create a graph with nodes representing the coordinates of the airports. Each node will have a unique identifier (e.g., A, B, C, etc.). The graph will have edges connecting the nodes, representing the possible flight paths.


Step 2: Add edges to the graph
For each flight, add edges to the graph connecting the nodes representing the coordinates of the airports. For example, for Flight 1, add edges between nodes A (1,1), B (2,2), and C (3,3).


Step 3: Find the shortest path for each flight
Use a shortest path algorithm (e.g., Dijkstra's algorithm ) to find the shortest path for each flight. This will give us the optimal flight path for each flight.


Step 4: Check for intersections
For each pair of flights, check if their shortest paths intersect. If they do, adjust the path of one of the flights to avoid the intersection. This can be done by adding a small detour to the path of one of the flights.


Step 5: Draw the flight paths
Using a visualization library (e.g., Matplotlib ), draw the flight paths for each flight. The resulting graph will show the individual flight paths without any intersections.


 Here's the output-

![Screenshot 2024-07-31 at 1 13 28 AM](https://github.com/user-attachments/assets/f7dceca6-90d6-417e-84c4-02b831e7282b)



 


This code creates a graph, adds nodes and edges, finds the shortest path for each flight, checks for intersections, and adjusts the paths if necessary. Finally, it draws the flight paths using Matplotlib. The resulting graph will show the individual flight paths without any intersections, ensuring safety and optimization.
