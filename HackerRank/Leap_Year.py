#Question Link :  https://www.hackerrank.com/challenges/write-a-function/problem

'''Pre-Requisite Knowledge:
  Concept of Leap Year :   
    Divisible by 4 → Leap Year ✅
    Divisible by 100 but not by 400 → Not a Leap Year ❌
    Divisible by 400 → Leap Year ✅
    ✅ Examples:
    2020 → Divisible by 4 → Leap Year
    1900 → Divisible by 100 but not 400 → Not a Leap Year
    2000 → Divisible by 400 → Leap Year'''


def is_leap(year):
    if(year% 100==0) and (year%400==0) :   
        return True  
    elif(year % 4==0) and (year% 100!=0):  
        return True 
    else :
        return False
year = int(input())
print(is_leap(year))  
