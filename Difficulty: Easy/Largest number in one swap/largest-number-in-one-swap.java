    /*
    Example Walkthrough (Right-to-left scan)
    Input - 2736

    i | digit | maxRight | action
    3 | 6     | 6        | maxIdx = 3
    2 | 3     | 6        | swap candidate (2,3)
    1 | 7     | 7        | maxIdx = 1
    0 | 2     | 7        | swap candidate (0,1)

    Final swap: (0,1)
    Result: 2736 → 7236
    */

class Solution {
    public String largestSwap(String s) {
        char [] arr = s.toCharArray();
        int n = arr.length;
        
        int maxIdx = n - 1;
        int left = -1;
        int right = -1;
        
        for(int i = n - 2; i >=0; i--){     // Traverse from right to left
            if(arr[i] > arr[maxIdx])
                maxIdx = i;                 // Update max digit index
            else if(arr[i] < arr[maxIdx]){  // If larger digit exists on right
                left = i;
                right = maxIdx;
            }
        }
        
        if(left != -1){                     // Perform swap
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
        
        return new String(arr);
    }
}