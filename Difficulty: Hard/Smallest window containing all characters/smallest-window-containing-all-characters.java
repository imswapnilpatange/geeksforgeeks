class Solution {
    public static String minWindow(String s, String p) {
        if(s.length() < p.length()) return "";
        
        // Step 1: Build requirement frequency
        int [] need = new int[256];                             // Size is 256 because indices are ASCII codes
        int distinctNeed = 0;
        
        for(char c : p.toCharArray()){
            if(need[c] == 0) distinctNeed++;
            need[c]++;
        }
        
        // Step 2: Sliding window state
        int [] have = new int[256];                                     // Size is 256 because indices are ASCII codes
        int formed = 0;
        
        int left = 0;
        int minLen = Integer.MAX_VALUE;
        int start = 0;
        
        // Step 3: Expand Window
        for(int right = 0; right < s.length(); right++){
            char c = s.charAt(right);
            have[c]++;
            
            if(need[c] > 0 && have[c] == need[c])                       // If character requirement is satisfied
                formed++;
                
            // Step 4: Shrink window while it remains valid
            while(formed == distinctNeed){                              // Current window = s[left..right] contains all required characters
                if(right - left + 1 < minLen){                          // Update minimum window if smaller
                    minLen = right - left + 1;
                    start = left;
                }
                
                char remove = s.charAt(left);                           // Remove leftmost character to attempt shrinking
                have[remove]--;                                         // Reduce count in window
                
                if(need[remove] > 0 && have[remove] < need[remove])     //If removal breaks requirement, then window becomes invalid.
                    formed--;                                           // Requirement of this character is no longer satisfied
                    
                left++;                                                 // Move left pointer to shrink the window
                
            }
            
        }

        // Step 5: Return Result
        if(minLen == Integer.MAX_VALUE) return "";
        return s.substring(start, start + minLen);
    }
}

/*
    Example
    s = "ADOBECODEBANC"
    t = "ABC"

    Need frequencies:
    A:1  B:1  C:1
    distinctNeed = 3

    Sliding Window Trace (Key Moments Only)

    String Index
    0 1 2 3 4 5 6 7 8 9 10 11 12
    A D O B E C O D E B  A  N  C

    |St|Act        |Win[l,r]|Substr     |frm|Expl           |
    |--|-----------|--------|-----------|---|---------------|
    |1 |r=0 add A  |[0,0]   |A          |1  |A satisfied    |
    |2 |r=3 add B  |[0,3]   |ADOB       |2  |B satisfied    |
    |3 |r=5 add C  |[0,5]   |ADOBEC     |3  |All found      |
    |4 |shrink     |[0,5→1] |DOBEC      |2  |A removed      |
    |5 |r=9 add B  |[1,9]   |DOBECODEB  |2  |B extra        |
    |6 |r=10 add A |[1,10]  |DOBECODEBA |3  |Valid again    |
    |7 |shrink     |[1→6,10]|ODEBA      |2  |C removed      |
    |8 |r=12 add C |[6,12]  |ODEBANC    |3  |Valid again    |
    |9 |shrink rep |[9,12]  |BANC       |3  |Smallest win   |
*/