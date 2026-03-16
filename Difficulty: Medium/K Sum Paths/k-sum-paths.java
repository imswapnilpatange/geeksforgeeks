/*
    FORMAL MODELING
    
    Let:
        prefix(u) = sum from root → node u
        For any downward path a → ... → b: sum(a..b) = prefix(b) − prefix(parent(a))
        We want: prefix(b) − prefix(parent(a)) = k
        Rearranging: prefix(parent(a)) = prefix(b) − k
    
    Therefore for every node b, if an earlier prefix sum equal to
    (prefix(b) − k) exists, then a valid downward path ending at b exists.
    
    INVARIANTS
    
    Prefix Sum Invariant
    --------------------
    During DFS traversal: map[x] = number of times prefix sum x appeared along the current root → node path.
    At node with prefix sum P: map[P − k] = number of valid starting nodes for paths ending at this node.
    
    Backtracking Invariant
    ----------------------
    After finishing both subtrees of a node: map[currentPrefix]--
    
    This removes the prefix contribution of that node so sibling
    subtrees do not incorrectly reuse prefix sums from another branch.
*/

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
import java.util.*;
class Solution {
    public int countAllPaths(Node root, int k) {
        Map<Long, Integer> map = new HashMap<>();                               //prefix sum → frequency
        map.put(0L, 1);                                                         //base case: prefix sum 0 occurs once
        
        return dfs(root, 0L, k, map);
    }
    
    private int dfs(Node node, long prefix, int k, Map<Long, Integer> map){
        if(node == null) return 0;
        prefix += node.data;                                                    //Step 1: Update prefix
        int count = map.getOrDefault(prefix - k, 0);                            //Step 2: Count valid paths ending here
        map.put(prefix, map.getOrDefault(prefix, 0) + 1);                       //Step 3: Record current prefix
        
        count += dfs(node.left, prefix, k, map);                                //Step 4a: Explore left child
        count += dfs(node.right, prefix, k, map);                               //Step 4b: Explore right child
        
        map.put(prefix, map.get(prefix) - 1);                                   //Step 5: Backtrack (remove prefix state)
    
        return count;
    }
}