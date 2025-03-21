'''
📄 Problem Statement:
You are given a list of days when you need to travel using public transport. Each day you travel requires a ticket, but you can choose between three types of passes:

1-day pass: Costs costs[0] and is valid for 1 day.

7-day pass: Costs costs[1] and is valid for 7 consecutive days.

30-day pass: Costs costs[2] and is valid for 30 consecutive days.

Your goal is to determine the minimum cost required to cover all the given travel days.

🎯 Goal:
Find the minimum cost to cover all travel days by choosing the best combination of the three types of passes.
'''
def cost(train_days,costs,n,day=0): #kono call e days pass na hole by default 0 nebe,else day er passed value
    # Base case: jodi current date last date er pore hoe. Ex- last date input dilam 28 but day 29 e chole gache
    if day>=n:
        return 0
    # If the current day is not in the travel days, move to the next day
    elif day not in train_days:
        return cost(train_days,costs,n,day+1)
    else:
        # 1.Buy a 1-day pass and calculate cost for the next day
        # 2.Buy a 7-day pass and calculate cost after 7 days
        # 3.Buy a 30-day pass and calculate cost after 30 days
        return min( costs[0]+cost(train_days,costs,n,day+1),  costs[1]+cost(train_days,costs,n,day+7),  costs[2]+cost(train_days,costs,n,day+30)   )

train_days=list(map(int,input("Enter days in which train is travelling ").split()))
costs=list(map(int,input("Enter costs ").split()))
n=int(input("Enter the last day "))
print(cost(train_days, costs, n))
