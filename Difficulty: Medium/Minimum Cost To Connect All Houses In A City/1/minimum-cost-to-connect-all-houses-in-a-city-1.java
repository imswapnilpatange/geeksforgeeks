class Solution {
    
    public int minCost(int[][] houses) {
        int n = houses.length;
        
        boolean[] visited = new boolean[n];
        int[] minDist = new int[n];                                     // min cost to connect each node
        Arrays.fill(minDist, Integer.MAX_VALUE);                        // Initialize with infinity 
        minDist[0] = 0;                                                 // start from node 0
        int totalCost = 0;
        
        for (int i = 0; i < n; i++) {                                   // Step 1: pick minimum cost unvisited node
            int u = -1;
            for (int j = 0; j < n; j++) {
                if (!visited[j] 
                && (u == -1 || minDist[j] < minDist[u]))
                    u = j;
            }

            visited[u] = true;                                          // Step 2: include it in MST
            totalCost += minDist[u];

            for (int v = 0; v < n; v++) {                               // Step 3: update distances
                if (!visited[v]) {
                    int dist = Math.abs(houses[u][0] - houses[v][0]) +
                               Math.abs(houses[u][1] - houses[v][1]);
                    
                    if (dist < minDist[v])
                        minDist[v] = dist;
                }
            }
        }
        
        return totalCost;
    }
}