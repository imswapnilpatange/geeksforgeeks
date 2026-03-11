class Solution {
    public int kBitFlips(int[] arr, int k) {
        int n = arr.length;
        
        int[] expire = new int[n];                      //Marks flip start positions
        int flipParity = 0;                             //Active flip parity
        int flips = 0;
        
        for(int i = 0; i < n; i++){
            if(i >= k) flipParity ^= expire[i - k];     //Step 1: Remove expired flip effect
            
            int effective = arr[i] ^ flipParity;        //Step 2: Compute effective bit
            
            if(effective == 0){                         //Step 3: If effective bit is 0, flip it
                if(i + k > n) return -1;
                
                flips++;
                flipParity ^= 1;                        //Activate flip
                expire[i] = 1;                          //Mark where flip started
                
            }
        }
        
        return flips;
    }
}
