class Solution(object):
    def generate(self, Rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if Rows==1:
            return [[1]]
        l=[[1]]
        for i in range(1,Rows):
            l1=[1]
            for j in range(1,i):
                l1.append(l[i-1][j-1]+l[i-1][j])
            l1.append(1)
            l.append(l1)
        return l
