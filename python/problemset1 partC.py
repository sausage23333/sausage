# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:38:08 2021

@author: Sausage
"""


import numpy 
import math
"""0<=portion_down_payment<=1
current_savings
r=0.04
months<=36
"""
months=1
current_savings=0
portion_down_payment=0.25
annual_salary=float(input("Enter the starting salary:​"))
portion_saved=0
total_cost=1000000
semi_annual_raise=0.07
high=1.0
low=0.0
search_number=0
current_savings=0
guess=(high+low)/2.0
while abs(current_savings-250000)>=100:
  
  current_savings=current_savings+annual_salary/12*guess
  if current_savings<250000:
     low=guess
  else:
     high=guess
  guess=(high+low)/2.0
  search_number+=1
print(current_savings)         
print("Steps in bisection search:",search_number)
print(high,low)
print(guess)
