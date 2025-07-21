'''
Problem Statement:

The problem statement for the "Stock Profit" section is not explicitly stated within the provided code comments or markdown. Based on the context and usual stock-related problems, here's a likely interpretation:

Given a list of stock prices for consecutive days, find the maximum profit that could have been made by buying and selling a single share of the stock. In other words, find the largest difference between a buying price and a selling price, but the selling day must come after the buying day.

Conditions:

You are given an array representing stock prices on different days.
You can only buy once and sell once.
You need to find the maximum profit achievable by buying and selling on specific days within the given period.
The selling day must come after the buying day.
'''

def maxFinder(Price):
  n=len(Price)
  minUptil=[]
  maxUptil=[]
  for i in range(0,n):
    if i==0:
      minUptil.append(Price[i])
    else:
      minUptil.append(min(minUptil[i-1],Price[i]))
    maxUptil.append(Price[i]-minUptil[i])  #KOM DAM E KINE PAST E BIKRI SOMBHOB NA
  print("minuptil",minUptil)
  print("maxUptil",maxUptil)
  print("ANS",max(maxUptil))




price = list(map(int,input("Enter Price ").split()))
maxFinder(price)