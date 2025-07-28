# Link-> https://leetcode.com/problems/longest-common-subsequence/
class Solution(object):
    def longestCommonSubsequence(self, s1, s2):
        m1=len(s1)
        m2=len(s2)
        l=[]
        for i in range(m1+1):
            l1=[]
            for j in range(m2+1):
                l1.append(0)
            l.append(l1)

        for i in range(1,m1+1):
            for j in range(1,m2+1):
                if s1[i-1]==s2[j-1]:
                    l[i][j]=l[i-1][j-1]+1
                else:
                    l[i][j]=max(l[i-1][j],l[i][j-1])
        return l[m1][m2]
        
