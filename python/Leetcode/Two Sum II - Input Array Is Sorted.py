class Solution:
    def twoSum(self, num: List[int], t: int) -> List[int]:
        l=[]
        for i in num:
            if (t-i) in num:
                l.append(num.index(i)+1)
                if i==t-i:
                    num.remove(i)
                    l.append(num.index(t-i)+2) 
                else:
                    l.append(num.index(t-i)+1)    
                return l
