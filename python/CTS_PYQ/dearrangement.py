```A Derangement is a permutation of n elements, such that no element appears in its original position. For example, a derangement of {0, 1, 2, 3} is {2, 3, 1, 0}. Given a number n, find the total number of Derangements of a set of n elements.

Input Specification:

Input 1: N, the number of Objects

Output Specification:

Return the number of arrangements in which no object occurs at its original position

Example 1:

Input: n = 2

Output: 1

For two elements say {0, 1}, there is only one possible derangement {1, 0}

Example 2:

Input: n = 3

Output: 2

For three elements say {0, 1, 2}, there are two possible derangements {2, 0, 1} and {1, 2, 0}

Example 3:

Input: n = 4

Output: 9

For four elements say {0, 1, 2, 3}, there are 9 possible derangements {1, 0, 3, 2} {1, 2, 3, 0} {1, 3, 0, 2}, {2, 3, 0, 1}, {2, 0, 3, 1}, {2, 3,1, 0}, {3, 0, 1, 2}, {3, 2, 0, 1} and {3, 2, 1, 0}
```
def get_permutations(s, answer='', result=None):
    if result is None:
        result = []

    if len(s) == 0:
        result.append(answer)
        return result

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        get_permutations(remaining, answer + ch, result)

    return result
n=4
num = '0123'
per= get_permutations(str(num))
print(per)
c=0
for i in per:
    cas=1
    for j in range(n):
        if (i[j])==num[j]:
            cas=0
            break
    if cas==1:
        c=c+1
        
print(c)
