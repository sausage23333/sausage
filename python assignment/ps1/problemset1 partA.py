# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:27:56 2021

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
while current_savings<=total_cost*portion_down_payment:
     current_money_without_interest=current_savings+annual_salary*portion_saved/12
     current_savings=current_savings+annual_salary*portion_saved/12+current_money_without_interest*0.04/12
     months+=1

print("Number of months:",months)
