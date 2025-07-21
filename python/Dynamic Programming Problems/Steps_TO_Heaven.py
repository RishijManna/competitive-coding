#condition -> we can jump either 1 step or 2step at a time

'''
Problem Statement
1. Staircase to Heaven

Problem Statement:

You are climbing a staircase. You can climb either 1 step or 2 steps at a time. The problem is to count the number of distinct ways you can climb to the top (n steps).

Conditions:

You can take either 1 step or 2 steps at a time.
You need to find the total number of distinct ways to reach the top.
'''
def staircase_to_heaven(n):
  ways=[0]*(n+1)
  ways[0]=1  #ways[0] = 1: There's one way to stay at the starting point—by doing nothing.
  ways[1]=1  #ways[1] = 1: There's one way to reach the first step—by taking a single step.
  for i in range(2,n+1):
    ways[i]=ways[i-1]+ways[i-2]  # aita korlam kano ki i-th place e ami i-1 or i-2 die aste pari. So i-th er val i-1 er possible step+ i-2 er possible steps die hobe
  print(ways)
  return ways[n]
n=int(input("Enter the number of steps: "))
print("No. of possible ways are:",staircase_to_heaven(n))