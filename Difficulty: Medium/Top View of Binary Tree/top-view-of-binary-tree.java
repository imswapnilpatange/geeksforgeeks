/*
class Node {
    int data;
    Node left, right;

    Node(int val) {
        this.data = val;
        this.left = null;
        this.right = null;
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
    public ArrayList<Integer> topView(Node root) {
        ArrayList<Integer> result = new ArrayList<>();
        if(root == null) return result;
        
        Map<Integer, Integer> map = new HashMap<>();        //Map: horizontal distance: node value
        Queue<Pair> queue = new LinkedList<>();             //BFS Queue
        
        int minHD = 0, maxHD = 0;
        
        queue.add(new Pair(root, 0));                       //Step 1: Initialize BFS
        
        while(!queue.isEmpty()){                            //Step 2: Level order Traversal
            Pair curr = queue.poll();
            Node node = curr.node;
            int hd = curr.hd;
            
            if(!map.containsKey(hd))
                map.put(hd, node.data);                     //Record first node at this HD
                
            minHD = Math.min(minHD, hd);                    //Update minHD
            maxHD = Math.max(maxHD, hd);                    //Update maxHD
            
            if(node.left != null)
                queue.add(new Pair(node.left, hd - 1));     //Step 3a: Traverse Left Child
                
            if(node.right != null)
                queue.add(new Pair(node.right, hd + 1));    //Step 3b: Traverse right Child
            
        }
        
        for(int i = minHD; i <= maxHD; i++)
            result.add(map.get(i));                         //Step 4: Build result from leftmost to rightmost
        
        return result;
    }
}