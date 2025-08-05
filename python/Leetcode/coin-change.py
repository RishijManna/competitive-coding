#https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self,l,v):
        dp=[100000]*(v+1)
        dp[0]=0
        for i in range(1,v+1):
            for j in l:
                if i>=j:
                    dp[i]=min(dp[i],dp[i-j]+1)

        if dp[v]==100000:
            return -1
        else:
            return dp[-1]
        
