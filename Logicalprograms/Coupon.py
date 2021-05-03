'''
@Author: Vishal Salaskar
@Date: 2021-02-30
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-30 
@Title : To play a tictactoe
'''

import random 


def randomCoupon():
"""
Description:
A random coupon function to calculate the number of random coupons
"""    
    try:
        number = int(input("Enter number of coupons "))
        couponcheck=[0 for coupon in range(number)]
        couponnumber = []
        for i in range(number):
            value = int(input("Enter coupon number "))
            couponnumber.append(value)
            couponnumber = sorted(couponnumber)
        randomcount = 0
        print(couponnumber)
        while(all(couponcheck)==False):
            randomnumber = random.randint(couponnumber[0],couponnumber[number-1])    
            randomcount+=1
            if randomnumber in couponnumber:
                for i in range(number):
                    if randomnumber == couponnumber[i]:
                        couponcheck[i] = 1
        print("random number count", randomcount)            
    except ValueError as e:
        print(e)

randomCoupon()