# Lab Report — [Dijkstra's Shortest Path] - Chapter 9

## Student Information

Name: [Annabel Shaw]
Date: [4/12/26]

## Algorithm Analysis: Dijkstra's Algorithm

- **What type of graph does this program build?** [multidirectional, weighted]
- **Why must all edge weights be non-negative for Dijkstra's to work?'** [Dijkstra only works if you don't have to restore a node ladder so it can not consider negative numbers.]
- Time Complexity (with simple array scan for min-node): O(n)
- Time Complexity (with a min-heap/priority queue): O(log n)

## Core Data Structures

| Structure|	Variable Name|	What It Stores|
|----|----|-----|
|Adjacency |dict|	graph	|
|Cost| table|	costs	|
|Parent |table|	parents	|
|Visited| list|	processed|	

## Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

|Iteration|	Current Node|	costs[A]|	costs[B]	|costs[C]	|costs[D]|	processed|
|----------|-------------|-----------|---------------|-----------|--------|---------|
|Init	— |					
|1	A (0)	|		A| 0|1|4|6|	A|	
|2	B (1)	|		B|-|0|2|6|A,B|		
|3	C (3)	|		C|-|-|0|3|A,B,C|		
|4	D (6)	|		D|-|-|-|0|A,B,C,D|	


Shortest path A to D: [A-B(1),B-C(2),C-D(3)]

Total cost: [6]

## Reflection Questions

1) **Why does the algorithm initialize all node costs to infinity except the start node?**
    [Until processed it will take infidelity to get to each node, but we are starting at the start node so we don't have to travel to it.]
2) **Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?**
    [You would not be able to start in a different area with the same graph if it was not multidirectional.]
3) **The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?**
    [Priority cue helps not to rescore nodes and helps to narrow the search to the quickest route to the end.]
4) **If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?**
    [Dijkstra only works if you don't have to rescore a node ladder so it can not consider negative numbers. Bellman-ford algorithm]
5) **How does the parent's dictionary allow path reconstruction? Why do we reverse the path at the end?**
    [Parents dictionary allows paths reconstruction though hosting all possible edges and paths needed to get to any point in the map. To recount the cost.]
6) **What happens when the source and destination are in disconnected components of the graph? How does the code detect this?**
    [It travels through surrounding nodes until locating the ending node.]
