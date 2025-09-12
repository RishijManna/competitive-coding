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
num = '21'
per= get_permutations(str(num))
per.sort()
c=0
for i in per:
    if int(num)<int(i):
        print(int(i))
        c=1
        break
if c==0:
    print(-1)
        
