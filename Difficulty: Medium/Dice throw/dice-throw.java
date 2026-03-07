    /*
    ===============================
    2. State Modeling
    ===============================
    dp[i][s] = number of ways to obtain sum s using i dice

    i → number of dice used
    s → target sum formed

    ===============================
    3. State Transition Formula
    ===============================
    For the i-th die we can roll values 1..M

    dp[i][s] = Σ dp[i-1][s-f]
               where f = 1..M and s-f ≥ 0

    Meaning:
    Previous dice must produce sum (s - f)
    Current die contributes value f

    ===============================
    7. Algorithm
    ===============================
    1. Check reachability:
       if (x < n || x > n*m) return 0

    2. Initialize DP table
       dp[0][0] = 1

    3. For each dice:
          for dice = 1..n
              for sum = 1..x
                  for face = 1..m
                      if sum-face ≥ 0
                          dp[dice][sum] += dp[dice-1][sum-face]

    4. Return dp[n][x]
    */
class Solution {
    static int noOfWays(int m, int n, int x) {
        if(x < n || x > m * n)                                     //Reachability Check
            return 0;
            
        int [][] dp = new int [n + 1][x + 1];
        dp[0][0] = 1;                                              //Base Case
        
        for(int dice = 1; dice <= n; dice++){                      //Iterate over dice
            for(int sum = 1; sum <= x; sum++){                     //Iterate over all possible sums
                for(int face = 1; face <= m; face++){              //Try over all face values
                    if(sum - face >= 0)
                        dp[dice][sum] += dp[dice - 1][sum - face];
                    
                }
            }
        }
        
        return dp[n][x];
    }
};