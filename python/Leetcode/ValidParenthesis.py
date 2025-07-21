#Link -> https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isValid(self, s):
        stack=[]
        
        for c in s:
            if c== "(" or c=="{" or c=="[":
                stack.append(c)
            elif c==")":
                if not stack or stack.pop()!="(":
                    return False
            elif c=="}":
                if not stack or stack.pop()!="{":
                    return False
            elif c=="]":
                if not stack or stack.pop()!="[":
                    return False   
        return not stack
