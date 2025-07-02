class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l =s.split()
        st=''
        for i in range(len(l)-1,-1,-1):
            st=st+l[i]
            if i!=0:
                st=st+' '
        return st
