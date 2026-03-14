/*
    Approach:
    Use BFS with horizontal distance (HD) tracking.
    
    HD rules:
    root → 0
    left child → hd - 1
    right child → hd + 1
    
    Perform level-order traversal using a queue storing (node, hd).
    Store node values in a TreeMap<hd, List> so columns remain sorted left→right.
    Because BFS is used, nodes appearing in the same vertical column automatically
    follow level-order ordering.
    
    Finally iterate the TreeMap and collect columns into the result list.
    
    Time Complexity:  O(N log N)
    Space Complexity: O(N)
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
class Pair{
    Node node;
    int hd;
    
    Pair(Node n, int h){
        node = n;
        hd = h;
    }
}

class Solution {
    public ArrayList<ArrayList<Integer>> verticalOrder(Node root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        if(root == null) return result;
        
        TreeMap<Integer, ArrayList<Integer>> map = new TreeMap<>();     //Maintain vertical columns sorted by horizontal distance
        
        Queue<Pair> queue = new LinkedList<>();                         //BFS Queue
        queue.offer(new Pair(root, 0));                                 //Initialize BFS queue
        
        while(!queue.isEmpty()){
            Pair curr = queue.poll();
            Node node = curr.node;
            int hd = curr.hd;
            
            map.putIfAbsent(hd, new ArrayList<>());                     //Add entry for hd if not present
            map.get(hd).add(node.data);                                 //Add node value for corresponding vertical column
            
            if(node.left != null)
                queue.offer(new Pair(node.left, hd - 1));               //Process left child
            
            if(node.right != null)
                queue.offer(new Pair(node.right, hd + 1));              //Process right child
        }
        
        for(ArrayList<Integer> col : map.values())                           //Build final result from leftmost to rightmost column
            result.add(col);
        
        return result;
    }
}