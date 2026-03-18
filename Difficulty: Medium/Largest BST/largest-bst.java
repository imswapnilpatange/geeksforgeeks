// Approach (O(N) - Postorder DFS):
// 1. For each node, return Info: {isBST, size, min, max}
// 2. Base case: null → BST, size=0, min=+INF, max=-INF
// 3. Traverse in postorder: get left & right Info
// 4. If (left.isBST && right.isBST && root.data > left.max && root.data < right.min):
//      → current subtree is BST
//      → size = left.size + right.size + 1  (include current node)
//      → update min/max
// 5. Else:
//      → not a BST
//      → size = max(left.size, right.size) (largest BST below)
// 6. Final answer = size from root Info

class Solution {

    static class Info {
        boolean isBST;
        int size;
        int min;
        int max;

        Info(boolean isBST, int size, int min, int max) {
            this.isBST = isBST;
            this.size = size;
            this.min = min;
            this.max = max;
        }
    }

    static int largestBst(Node root) {
        return solve(root).size;
    }

    static Info solve(Node root) {

        if (root == null) {
            return new Info(true, 0, Integer.MAX_VALUE, Integer.MIN_VALUE);
        }

        Info left = solve(root.left);
        Info right = solve(root.right);

        if (left.isBST && right.isBST &&
            root.data > left.max && root.data < right.min) {

            return new Info(
                true,
                left.size + right.size + 1,
                Math.min(root.data, left.min),
                Math.max(root.data, right.max)
            );
        }

        return new Info(false, Math.max(left.size, right.size), 0, 0);
    }
}