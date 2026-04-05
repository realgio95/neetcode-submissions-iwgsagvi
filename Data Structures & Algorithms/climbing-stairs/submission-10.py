class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 1 2 3 5 8
        val = n + 1
        dp = [1] * val

        i = 2
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2]
            i+=1         
        
        return dp[n]
        

    