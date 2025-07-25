#LInk->https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
class Solution(object):
    def minMovesToMakePalindrome(self, arr):
        
        left=0
        right=len(arr)-1
        merges=0

        while left<right:
            if arr[left]==arr[right]:
                left+=1
                right-=1
            elif arr[left]<arr[right]:
                arr[left+1]+=arr[left]
                left+=1
                merges+=1
            else:
                arr[right-1]+=arr[right]
                right-=1
                merges+=1

        return merges
        
