
'''
📊 Problem Statement: Prefix Sum and Range Sum Query
Given an array of integers, you are required to:

Compute the prefix sum array where each element at index i contains the sum of all elements from the start up to i.
Find the sum of elements between a given range [start, end] efficiently using the prefix sum array.
Goal:
Calculate the sum of elements in the specified range using prefix sum logic to optimize the query.

Input:
An array of integers.
Two integers start and end representing the range.
Output:
The prefix sum array.
The sum of elements between the indices start and end.
Constraints:
If start = 0, return the prefix sum at end.
Otherwise, return the difference between sum_until[end] and sum_until[start - 1].
'''


# Function to compute the prefix sum array
def cal(arr):
    n=len(arr)                                                                  # Get the length of the input array
    sum_until=[0]*n                                                             # Initialize an array to store prefix sums
    sum_until[0]=arr[0]                                                         # First element remains the same
    for i in range(1,n):
        sum_until[i]=sum_until[i-1]+arr[i]                                      # Add current element to previous sum
    return sum_until                                                            #Return the prefix sum array

# Function to get the sum of elements in a given range (start to end)
def ranger(sum_until,start,end):
    if start==0:
        return sum_until[end]                                                   # If start is 0, return the prefix sum at index 'end'
    else:
        return sum_until[end]-sum_until[start-1]                                # Subtract prefix sum before 'start' from sum_until[end]

arr=list(map(int,input("Enter array elements: ").split()))                      # Read space-separated integers as an array
s,e=map(int,input("Enter the start and end range: ").split())                   # Read start and end indices
sum_until_arr=cal(arr)                                                          # Compute prefix sum array
print("Sum Untill Array: ",sum_until_arr)
result=ranger(sum_until_arr,s,e)                                                # Compute the sum of elements in the given range
print(result) 