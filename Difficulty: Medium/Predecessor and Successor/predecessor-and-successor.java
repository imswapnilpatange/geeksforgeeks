/*
class Node {
    int data;
    Node left, right;
    Node(int x) {
        data = x;
        left = right = null;
    }
}
*/

class Solution {
    public ArrayList<Node> findPreSuc(Node root, int key) {
       
       
       ArrayList<Node>answer=new ArrayList<>();
       
       Node p=null;
       Node s=null;
       
       while(root!=null){
            if(root.left==null){
                
                 if(root.data<key){
                     p=root;
                  }
                 if(root.data>key){
                     s=root;
                     break;
                  }
                 root=root.right;
            } else {
                 Node curr=root.left;
                 while(curr.right!=null && curr.right!=root)
                       curr=curr.right;

                 if(curr.right==null){
                      curr.right=root;
                      root=root.left;
                 } else {
                     curr.right=null;
                     if(root.data<key) p=root;
                     if(root.data>key){
                         s=root;
                         break;
                     }
                     root=root.right;
                 }
            }
       }
       
       answer.add(p);
       answer.add(s);
       
       return answer;
    }
}

