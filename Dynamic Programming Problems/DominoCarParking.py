''' 
🧩 Problem Statement: Domino Tiling Problem
You are tasked with finding the number of ways to completely fill a 2 × n grid using 2 × 1 domino tiles. Each tile can be placed either vertically or horizontally.

Goal:
Determine how many ways the grid can be tiled using dominoes.

Input:
An integer n representing the length of the grid.
Output:
An integer representing the number of ways to tile the 2 × n grid.
Constraints:
The grid can be filled by:
Placing one vertical domino in the first column and filling the remaining 2 × (n-1) grid.
Placing two horizontal dominoes to fill the first two rows and covering the remaining 2 × (n-2) grid.
'''



def domino(n):
  ways=[0]*(n+1)   # Initialize a list to store the number of ways to fill up to n units
  ways[0]=1  # length 0 ke koto bhabe arrange korte pari??? Ans- 1 way i.e. doing nothing
  ways[1]=1   # Base case: 1 way to fill a 1-length (using one vertical domino)
  for i in range(2,n+1):
    ways[i]=ways[i-1]+ways[i-2]    # - ways to fill length (i-1) and place a vertical domino   ways to fill length (i-2) and place two horizontal dominoes
  print(ways)
  return ways[n]

n=int(input("Enter the number of cars: "))
print(domino(n))