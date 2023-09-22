"""
Description: Resubmission of Assignment 2
Author: Tanvir Singh Bhullar
Date: 22/09/2023
Usage:Python and Variables
"""


#SIMPLE DATA TYPES


name = "Tanvir Singh Bhullar"
print("value:",name)
print(type(name))

Manitoba_License= "True"
print("value:",Manitoba_License)
print(type(Manitoba_License))

year= 2023
print("value:",year)
print(type(year))

next_year= year + 1
print("next:", next_year, "type", type(next_year))

#CALCULATIONS

GOODS_AND_SERVICE_TAX_RATE = 0.05
PROVINCIAL_SALES_TAX = 0.07
price_of_a_vehicle = 99997

GST = price_of_a_vehicle * GOODS_AND_SERVICE_TAX_RATE
PST = price_of_a_vehicle * PROVINCIAL_SALES_TAX
final_cost_of_vehicle  = price_of_a_vehicle + GST + PST

print("pre-tax value:", price_of_a_vehicle, "PST:", PST, "GST:", GST, "total:", final_cost_of_vehicle)
print(f"pre-tax value: ${price_of_a_vehicle: .2f} PST:{PST: .2f} GST:{GST: .2f} total: ${final_cost_of_vehicle: .2f}")

#LISTS

#TUPLES

#DICTIONARIES

#SETS

