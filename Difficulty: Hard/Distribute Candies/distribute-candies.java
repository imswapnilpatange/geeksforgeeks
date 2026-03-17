/*
class Node {
    int data;
    Node left;
    Node right;
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}
*/

class Solution {
    int moves = 0;
    public int distCandy(Node root) {
        dfs(root);
        return moves;
    }
    private int dfs(Node node){
        if(node == null) return 0;
        
        int left = dfs(node.left);                  //Step 1a: comute left child
        int right = dfs(node.right);                //Step 1b: comute right child
        
        moves += Math.abs(left) + Math.abs(right);  //Step 2: moves needed to balance children
        
        int excess = node.data + left + right - 1;  //Step 3: Comute node access
        
        return excess;
    }
}