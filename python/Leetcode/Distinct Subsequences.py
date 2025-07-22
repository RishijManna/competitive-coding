#Link ->  https://leetcode.com/problems/distinct-subsequences/


class Solution(object):
    def numDistinct(self,s,t):
        m=len(s) 
        n=len(t)  
        dp=[]
        for i in range(m + 1):
            l= []
            for j in range(n + 1):
                l.append(0)
            dp.append(l)
            
        for i in range(m + 1):
            dp[i][0]=1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[m][n]

        
