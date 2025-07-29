#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def maxProfit(self, prices):
        ans=0
        n=len(prices)
        for i in range(1,n):
            if prices[i-1]<prices[i]:
                ans+=prices[i]-prices[i-1]
        return ans
