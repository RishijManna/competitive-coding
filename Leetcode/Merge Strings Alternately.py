class Solution(object):
    def mergeAlternately(self, word1, word2):
        l1=len(word1)
        l2=len(word2)
        c1,c2=0,0
        s1=''
        while(c1<l1 and c2<l2):
            s1 = s1+word1[c1]
            s1 = s1+word2[c2]
            c1=c1+1
            c2=c2+1
        if c1<l1:
            s1=s1+word1[c1:]
        elif c2<l2:
            s1=s1+word2[c2:]
        return s1
