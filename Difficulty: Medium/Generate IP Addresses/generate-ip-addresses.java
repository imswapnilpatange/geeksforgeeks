/*
    State Modeling:
    - Input string s of length n must be split into 4 segments using 3 dots.
    - Each segment length ∈ [1,3].
    - Valid IP possible only if: 4 ≤ n ≤ 12.
    
    State Transition:
    - Build segments sequentially.
    - From index i choose length ∈ {1,2,3}.
    - Next state → (index + length, segment + 1).
    
    Invariants:
    1. Segment value must satisfy 0 ≤ value ≤ 255.
    2. Leading zero rule: if s[i] == '0', only length = 1 allowed.
    3. Remaining feasibility: for remaining segments k and chars rem → k ≤ rem ≤ 3k.
    
    Reachability:
    - If n < 4 or n > 12 → no valid IP address possible.
*/

import java.util.ArrayList;
class Solution {
    public ArrayList<String> generateIp(String s) {
        ArrayList<String> result = new ArrayList<>();
        int n = s.length();
        
        if(n < 4 || n > 12) return result;                                      //Check reachability constraint
        
        backtrack(s, 0, 0, new StringBuilder(), result);
        
        return result;
    }
    
    private void backtrack(String s, int index, int segment, 
            StringBuilder current, ArrayList<String> result){
                
        int n = s.length();
        if(segment == 4){                                                       //If 4 segments are used
            if(index == n)                                                      //Accept only if entire string is consumed
                result.add(current.substring(0, current.length() - 1));
                
            return;
        }
        
        int remainingChars = n - index;
        int remainingSeg = 4 - segment;
        
        if(remainingChars < remainingSeg || remainingChars > remainingSeg * 3)  //Prune unreachable states
            return;
            
        int value = 0;
        for(int len = 1; len <= 3 && index + len <= n; len++){  
            char c = s.charAt(index + len - 1);
            value = value * 10 + (c - '0');
            
            if(value > 255) break;                                              //Check octet bound
            if(len > 1 && s.charAt(index) == '0') break;                        //Leading 0 rule
            
            int prevLength = current.length();
            current.append(value).append('.');
            
            backtrack(s, index + len, segment + 1, current, result);            //Recurse
            
            current.setLength(prevLength);                                      //Backtrack
        }
    }
}