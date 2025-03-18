'''
🏡 Problem Statement: House Robber Problem
A professional robber is planning to rob houses along a street. Each house has a certain amount of money stashed, and the robber cannot rob two adjacent houses due to security alarms.

Goal:
Determine the maximum amount of money the robber can steal without alerting the police.

Input:
A list of integers representing the amount of money available in each house.
Output:
An integer representing the maximum amount of money the robber can rob.
Constraints:
The robber can choose to either:
Rob the current house and skip the next one.
Skip the current house and move to the next one.
'''



def rob_house(houses,n):
  if n==0:  # If there are no houses, return 0 (nothing to rob)
    return 0

  # max_money[i] Actually Represents -> stores the highest profit that can be earned from house i to the last house (n-1).
  '''max_money[0] = 41 → Max money from house 0 to 6.
  max_money[1] = 41 → Max money from house 1 to 6.
  max_money[2] = 34 → Max money from house 2 to 6.
  max_money[3] = 34 → Max money from house 3 to 6.
  max_money[4] = 12 → Max money from house 4 to 6.
  max_money[5] = 4 → Max money from house 5 to 6.
  max_money[6] = 4 → Max money from house 6 only.
  '''
  max_money=[0]*(n+1)   # This will store the maximum money that can be robbed starting from each house
  max_money[n]=0    # No houses left beyond 'n', so set max_money[n] to 0
  max_money[n-1]=houses[n-1]  # If only one house is left (last house), the thief will rob it

  for i in range(n-2,-1,-1):
      # Two choices at house 'i':
        # 1. Rob this house and add money from 'i+2' (since adjacent houses can't be robbed)
        # 2. Skip this house and take the max money from the next house ('i+1')
    max_money[i]=max(houses[i]+max_money[i+2],max_money[i+1])
    print("MAX MONEY: ", max_money)
  return max_money[0]

houses=list(map(int,input("Enter assests cost of each house").split()))
print("HOUSES: ",houses)
print("ANS",rob_house(houses,len(houses)))