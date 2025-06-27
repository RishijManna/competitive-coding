Container With Most Water

def maxw(height):
    left,right=0,len(height)-1
    maxwater=0
    while left<right:
        width=right-left
        min_h=min(height[left],height[right])
        area=width*min_h
        maxwater=max(maxwater,area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxwater
n=int(input())
height=list(map(int,input().split()))
print(maxw(height))
