    /*
    Example
    -------
    Input: arr = [1, 3, 5, 2]
    Output: 8

    For-Loop Execution
    ------------------

    | i | arr[i] | stack-before | idx | ans | stack-after |
    |---|--------|--------------|-----|-----|-------------|
    | 0 | 1      | []           | -   | 0   | [0]         |
    | 1 | 3      | [0]          | -   | 0   | [0,1]       |
    | 2 | 5      | [0,1]        | -   | 0   | [0,1,2]     |
    | 3 | 2      | [0,1,2]      | 2   | 1   | [0,1]       |
    | 3 | 2      | [0,1]        | 1   | 3   | [0]         |
    | 3 | 2      | [0]          | -   | 3   | [0,3]       |

    Remaining Stack Resolution
    --------------------------

    pop 3 → ans += (4-3) = 1 → ans = 4
    pop 0 → ans += (4-0) = 4 → ans = 8

    Approach
    --------
    Use a monotonic increasing stack to find the Next Smaller Element to the right.
    */

import java.util.Stack;
class Solution {
    public int countSubarrays(int[] arr) {
        int n = arr.length;
        int ans = 0;
        
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < n; i++){
            while(!stack.empty() && arr[i] < arr[stack.peek()]){
                int idx = stack.pop();
                ans += i - idx;
            }
            stack.push(i);
        }
        
        while(!stack.empty()){
            int idx = stack.pop();
            ans += n - idx;
        }
        
        return ans;
    }
}
