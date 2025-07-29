#leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        try:
            i=nums.index(target)
            return i
        except:
            return -1
