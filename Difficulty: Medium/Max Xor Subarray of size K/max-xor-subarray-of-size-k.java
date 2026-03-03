class Solution {
    public int maxSubarrayXOR(int[] arr, int k) {

        if(arr == null || arr.length == 0 || k > arr.length)    // Edge Case
            return 0;
            
        int windowXor = 0;
        for(int i = 0; i < k; i++)
            windowXor ^= arr[i];                                // Xor first k elements
        
        int n = arr.length;
        int maxXor = windowXor;
        for(int i = k; i < n; i++){
            windowXor ^= arr[i - k];                        // Outgoing element
            windowXor ^= arr[i];                            // Incoming element
            maxXor = Math.max(maxXor, windowXor);           // Updating max
        }
        
        return maxXor;
    }
}
