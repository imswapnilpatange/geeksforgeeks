import java.util.HashMap;

class Solution {

    public int totalElements(int[] arr) {

        // Check null or empty input
        if (arr == null || arr.length == 0)
            return 0;

        int left = 0;
        int maxLength = 0;

        // Map to maintain fruit frequency inside window
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int right = 0; right < arr.length; right++) {

            // Add current fruit to window
            freq.put(arr[right], 
                     freq.getOrDefault(arr[right], 0) + 1);

            // If more than 2 distinct arr, shrink window
            while (freq.size() > 2) {

                freq.put(arr[left], 
                         freq.get(arr[left]) - 1);

                // Remove fruit type if count becomes 0
                if (freq.get(arr[left]) == 0) {
                    freq.remove(arr[left]);
                }

                left++;  // Move left pointer
            }

            // Update maximum window length
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}