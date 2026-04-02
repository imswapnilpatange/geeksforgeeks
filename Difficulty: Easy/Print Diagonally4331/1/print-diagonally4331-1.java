class Solution {
    static ArrayList<Integer> diagView(int mat[][]) {
        int n = mat.length;
        ArrayList<Integer> res = new ArrayList<>();
        
        // Phase 1: Start from first row
        for (int col = 0; col < n; col++) {
            int i = 0, j = col;
            
            // Traverse current diagonal
            while (i < n && j >= 0) {
                res.add(mat[i][j]);
                
                // Move down-left
                i++;
                j--;
            }
        }
        
        // Phase 2: Start from last column (excluding first row)
        for (int row = 1; row < n; row++) {
            int i = row, j = n - 1;
            
            // Traverse current diagonal
            while (i < n && j >= 0) {
                res.add(mat[i][j]);
                
                // Move down-left
                i++;
                j--;
            }
        }
        
        return res;
    }
}