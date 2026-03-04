class Solution {
    public int longestKSubstr(String s, int k) {
        if(s == null || s.length() == 0 || k == 0)
            return -1;
            
        int n = s.length();
        int [] freq = new int[26];
        
        int left = 0;
        int distinct = 0;
        int maxLen = -1;
        
        // Expand window using right operator
        for(int right = 0; right < n; right++){
            int idx = s.charAt(right) - 'a';
            
            // Add character
            if(freq[idx] == 0) distinct++;
            freq[idx]++;
            
            // Shrink while distinct > k
            while(distinct > k){
                int leftIdx = s.charAt(left) - 'a';
                freq[leftIdx]--;
                
                if(freq[leftIdx] == 0)
                    distinct--;
                    
                left++;
            }
            
            // Check exact k distinct
            if(distinct == k)
                maxLen = Math.max(maxLen, right - left + 1);
            
        }
        
        return maxLen;
    }
}