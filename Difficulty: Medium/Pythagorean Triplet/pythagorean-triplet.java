import java.util.*;

class Solution {
    boolean pythagoreanTriplet(int[] arr) {
        
        HashSet<Integer> set = new HashSet<>();
        
        // store squares
        for(int num : arr){
            set.add(num * num);
        }
        
        int n = arr.length;
        
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                
                int sum = arr[i] * arr[i] + arr[j] * arr[j];

                if(set.contains(sum))
                    return true;
            }
        }
        
        return false;
    }
}