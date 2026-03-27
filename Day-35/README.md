# Day 35: Minimum Height Roots

## 🔗 Problem Link
https://www.geeksforgeeks.org/problems/minimum-height-roots/1

## 💡 Problem Logic
* Observation: To minimize the height of a tree, the root must be as "central" as possible. A tree can have at most two such centers (centroids).
* Strategy: Used a Topological Sort / BFS-based Pruning approach. By identifying all leaf nodes (nodes with degree 1) and removing them layer by layer, we eventually narrow down the graph to its center(s). This is similar to Kahn's algorithm but applied to an undirected tree.
* Edge Cases: Handled the case where V = 1 by immediately returning node 0, as it is the only possible root.



## 📊 Complexity Analysis
* Time Complexity: O(V) — We traverse each vertex and edge once during the adjacency list creation and the leaf pruning process.
* Space Complexity: O(V) — Required to store the adjacency list, the degree of each node, and the queue for BFS.

---
## ✅ Verification
![Test Case Result](../assets/Day35_24March.png)
*Passed all test cases on GeeksforGeeks.*