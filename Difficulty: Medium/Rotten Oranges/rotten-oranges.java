/**
 * Step-by-Step Thought Process:
 *
 * 1. Approach:
 *    - Traverse the grid:
 *        • Add all rotten oranges (2) into a queue.
 *        • Count total fresh oranges.
 *
 *    - Perform BFS:
 *        • Process nodes level by level (each level = 1 minute).
 *        • For each rotten orange:
 *            → Check 4 directions.
 *            → If fresh orange found:
 *                - Convert it to rotten.
 *                - Add to queue.
 *                - Decrease fresh count.
 *
 *    - Increment time after processing each level.
 *
 * 2. Final Decision:
 *    - If all fresh oranges are rotted → return time.
 *    - If some fresh oranges remain → return -1.
 *
 * 3. Edge Cases:
 *    - No fresh oranges initially → return 0.
 *
 * 4. Complexity:
 *    - Time: O(N × M) → each cell processed once.
 *    - Space: O(N × M) → queue in worst case.
 */
 
class Solution {
    public int orangesRot(int[][] mat) {
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};                          // Step 1a: Setup Directions
        Queue<int[]> rotton = new LinkedList<>();                                   // Step 1b: Setup Queue
        int fresh = 0;
        
        for(int i = 0; i < mat.length; i++){                                        // Step 2: Traverse Grid (Initialize Queue + Count Fresh Oranges)
            for(int j = 0; j < mat[0].length; j++){
                if(mat[i][j] == 2) rotton.offer(new int[]{i, j});
                else if(mat[i][j] == 1) fresh++;
            }
        }
        
        if(fresh == 0) return 0;                                                    // Edge Case

        int time = 0;
        while(!rotton.isEmpty() && fresh > 0){                                      // Step 3: BFS Traversal (Minute Simulation)
            int size = rotton.size();
            
            for(int i = 0; i < size; i++){
                int[] curr = rotton.poll();
                
                for(int [] d: dirs){
                   int ni = curr[0] + d[0];
                   int nj = curr[1] + d[1];
                   
                   if(ni >= 0 && nj >= 0 && ni < mat.length && nj < mat[0].length   // check bounds
                        && mat[ni][nj] == 1){                                       // check fresh orange
                       mat[ni][nj] = 2;                                             // rot the orange
                       fresh--;
                       rotton.offer(new int[]{ni, nj});
                   }
                }
            }
            
            time++;                                                                 // increment time after each level
        }
        
        return fresh == 0 ? time : -1;                                              // Step 4: Final Check
    }
}