# https://leetcode.com/problems/rabbits-in-forest/submissions/1719797445/
class Solution(object):
    def numRabbits(self, ans):
        f={}
        t=0
        for i in ans:
            if i==0:
                t+=1  
            elif i not in f:
                f[i]=1 
                t+=i+1  
            else:
                f[i]+=1
                if f[i]>i+1:
                    f[i]=1
                    t+=i+1
        return t
