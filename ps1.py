#!/usr/bin/env python3
# encoding: utf-8

# Part A
annual_salary = float(input("Annual salary: $"))
portion_saved = float(input("Percentage of salary to save: "))/100
total_cost = float(input("Total cost: $"))

rate = 0.04

current_savings = 0.0
month = 0

while current_savings < total_cost:
    month += 1
    current_savings += (portion_saved*annual_salary/12)
    current_savings += (rate/12)*current_savings

print("Months to save for home: " + str(month))
