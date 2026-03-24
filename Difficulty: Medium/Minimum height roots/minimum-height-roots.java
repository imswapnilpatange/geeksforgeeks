import java.util.*;

class Solution {
    // The driver code specifically looks for the singular name "minHeightRoot"
    public ArrayList<Integer> minHeightRoot(int V, int[][] edges) {
        if (V == 1) {
            ArrayList<Integer> res = new ArrayList<>();
            res.add(0);
            return res;
        }

        // 1. Build Adjacency List and Track Degrees
        List<Set<Integer>> adj = new ArrayList<>();
        int[] degree = new int[V];
        for (int i = 0; i < V; i++) {
            adj.add(new HashSet<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
            degree[u]++;
            degree[v]++;
        }

        // 2. Identify Initial Leaf Nodes
        Queue<Integer> leaves = new LinkedList<>();
        for (int i = 0; i < V; i++) {
            if (degree[i] == 1) {
                leaves.offer(i);
            }
        }

        // 3. Iteratively Remove Leaves to Find Centroids
        int remainingNodes = V;
        while (remainingNodes > 2) {
            int leafCount = leaves.size();
            remainingNodes -= leafCount;
            for (int i = 0; i < leafCount; i++) {
                int leaf = leaves.poll();
                for (int neighbor : adj.get(leaf)) {
                    // Update degree of neighbor and check if it becomes a leaf
                    degree[neighbor]--;
                    if (degree[neighbor] == 1) {
                        leaves.offer(neighbor);
                    }
                }
            }
        }

        // 4. Return the remaining 1 or 2 nodes as an ArrayList
        return new ArrayList<>(leaves);
    }
}
