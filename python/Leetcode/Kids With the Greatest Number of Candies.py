class Solution(object):
    def kidsWithCandies(self, candies, eC):
        m=max(candies)
        L=[]
        for i in candies:
            if i+eC>=m:
                L.append(True)
            else:
                L.append(False)
        return L
