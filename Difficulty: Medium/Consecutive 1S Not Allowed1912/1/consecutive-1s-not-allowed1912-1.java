class Solution {
    int countStrings(int n) {

        if (n == 1) return 2;
        if (n == 2) return 3;

        long prev2 = 2; // dp[1]
        long prev1 = 3; // dp[2]

        for (int i = 3; i <= n; i++) {
            long curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }

        return (int) prev1;
    }
}