

#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeDuplicates(self, nums):
        l=[]
        c=0
        for i in nums:
            if l.count(i)<2:
                l.append(i)
                nums[c]=i
                c+=1
        
        return c
        
