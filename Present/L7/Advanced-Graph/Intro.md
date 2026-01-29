# Advanced Graph

## Overview

This section covers advanced graph algorithms for finding shortest paths, minimum spanning trees, topological ordering, and heuristic search techniques essential for solving complex graph problems.

## Topics

### Dijkstra's
Advanced Algorithms

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. Using a priority queue, it efficiently explores vertices in order of increasing distance from the source. Understanding Dijkstra's algorithm is essential for solving shortest path problems in networks, routing, and navigation systems.

### Prim's
Advanced Algorithms

Prim's algorithm constructs a minimum spanning tree by starting from an arbitrary vertex and repeatedly adding the minimum-weight edge that connects a vertex in the tree to a vertex outside the tree. This greedy approach efficiently finds the minimum spanning tree for connected weighted graphs. Mastering Prim's algorithm is crucial for network design and optimization problems.

### Kruskal's
Advanced Algorithms

Kruskal's algorithm builds a minimum spanning tree by sorting all edges by weight and adding them in order, skipping edges that would create cycles. Using union-find data structure, it efficiently detects cycles and constructs the MST. Understanding Kruskal's algorithm is essential for solving problems requiring optimal network connectivity with minimum total cost.

### Topological Sort
Advanced Algorithms

Topological sort orders vertices in a directed acyclic graph such that for every directed edge, the source vertex comes before the destination vertex. This ordering is essential for scheduling problems, dependency resolution, and determining execution order. Mastering topological sort is crucial for solving problems involving prerequisites, build systems, and task scheduling.

### A*
Advanced Algorithms

A* is a heuristic search algorithm that finds the shortest path between nodes using both the actual distance from the start and an estimated distance to the goal. By combining Dijkstra's approach with informed heuristics, A* efficiently explores the most promising paths first. Understanding A* is essential for pathfinding in games, robotics, and AI applications where optimal paths are required.

## Resources

- [Dijkstra's Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Prim's Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)
- [Kruskal's Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
- [Topological Sorting - GeeksforGeeks](https://www.geeksforgeeks.org/topological-sorting/)
- [A* Search Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/a-search-algorithm/)
- [Graph Algorithms - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/graph-algorithms/)
- [DSA Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
