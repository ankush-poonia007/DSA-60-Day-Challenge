# Day 36: Number of Ways to Arrive at Destination

## 🔗 Problem Link
[GeeksforGeeks POTD](https://www.geeksforgeeks.org/problems/number-of-ways-to-arrive-at-destination/1)

## 💡 Problem Logic
* **Observation**: This problem requires finding the shortest path distance AND the count of paths achieving that distance. A standard Dijkstra's algorithm finds the distance, but we need to maintain a `ways` array to count paths.
* **Strategy**: Modified **Dijkstra's Algorithm** with a DP-like update rule:
    1. If we find a **shorter** path to a neighbor: Update the distance and *reset* the ways to the parent's count.
    2. If we find an **equal** distance path: *Add* the parent's ways to the neighbor's ways (modulo $10^9 + 7$).
* **Edge Cases**: Handling the modulo at every addition and ensuring the heap only processes a node if the popped distance is currently the minimum (`d > dist[u]`).



## 📊 Complexity Analysis
* **Time Complexity**: $O(E \log V)$ — Standard Dijkstra complexity where $E$ is the number of edges and $V$ is vertices, due to the min-heap operations.
* **Space Complexity**: $O(V + E)$ — To store the adjacency list, distance array, and ways array.

---
## ✅ Verification
![Test Case Result](../assets/Day36_25March.png)
*Passed all test cases on GeeksforGeeks.*