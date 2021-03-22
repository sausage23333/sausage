# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:12:19 2021

@author: Sausage
"""

import pandas
import numpy 
import math
"""portion_down_payment=0.25
current_savings
r=0.04
"""
months=0
current_savings=0
portion_down_payment=0.25
annual_salary=float(input("Enter your annual salary:​"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
semi_annual_raise=float(input("Enter the percent of your semi annual raise, as a decimal:"))
while current_savings<=total_cost*portion_down_payment:
     current_money_without_interest=current_savings+annual_salary*portion_saved/12
     current_savings=current_savings+annual_salary*portion_saved/12+current_money_without_interest*0.04/12
     months+=1
     if months%6==0:
        annual_salary=annual_salary+annual_salary*semi_annual_raise
         

print("Number of months:",months)
