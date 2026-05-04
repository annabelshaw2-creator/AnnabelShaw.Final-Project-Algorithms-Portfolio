Lab Report — Dijkstra's Shortest Path

Student Information

Name: [Annabel Shaw]
Date: [4/12/26]
Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build? [multidirctonal, weighted]
Why must all edge weights be non-negative for Dijkstra's to work?' [Dijkstra only works if you dont have to resore a node lader so it can not consider negitive numbers]
Time Complexity (with simple array scan for min-node): O(n)
Time Complexity (with a min-heap/priority queue): O(log n)
Core Data Structures

Structure	Variable Name	What It Stores
Adjacency dict	graph	
Cost table	costs	
Parent table	parents	
Visited list	processed	
Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration	Current Node	costs[A]	costs[B]	costs[C]	costs[D]	processed
Init	—					
1	A (0)					
2	B (1)					
3	C (3)					
4	D (6)					
Shortest path A to D: [A-B(1),B-C(2),C-D(3)]
Total cost: [6]

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?
    [untill procesed it will take infidity to get to each node, but we are starting at the start node so we dont have to travle to it]
Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?
    [you would not be able to start in a difrent area with the same gragh if it was not multidirctonal]
The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?
    [Prioryt cue helps not to rescore nodes and helps to narow the seach to the quickest rote to the end]
If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?
    [Dijkstra only works if you dont have to rescore a node lader so it can not consider negitive numbers. Bellman-ford algorithm]
How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?
    [parents dictionary allow paths reconstruction though hosting all possable eges and paths needed to get to any ponit in the map. To recount the cost]
What happens when the source and destination are in disconnected components of the graph? How does the code detect this?
    [It travlels through sourounding nodes untill locating the ending node]
