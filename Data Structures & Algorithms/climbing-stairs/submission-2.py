class Solution:
    def climbStairs(self, n: int) -> int:

        # Create teh dynamic programing array

        dp = [0] * n
        
        # base case 
        if n == 1:
            return 1

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp)

        return dp[n - 1]


