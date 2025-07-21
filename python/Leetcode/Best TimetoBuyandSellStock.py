class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n= len(prices)
        minUptil=[]
        mini= prices[0]
        for i in range(0,n):
            if i==0:
                minUptil.append(prices[i])
            else:
                mini= min(mini,prices[i])
                minUptil.append(mini)
    
        maxUptil=[]
        for i in range(0,n):
            maxUptil.append(prices[i]-minUptil[i])
        return (max(maxUptil))
        
