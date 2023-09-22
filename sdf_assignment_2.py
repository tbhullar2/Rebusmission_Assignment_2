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
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("datatype:", type(integers))
print("integers:", integers)

# add first name between 5 and 6
integers.insert(5,"Tanvir")
print("integers:",integers)

# remove 9
integers.remove(9)
print(integers)

second_integers = ["A" , "B" , "C"]

#  combine first and second integers
third_integers = [integers, second_integers]

print("third integers:", third_integers)

#TUPLES
canada_provinces = ("Manitoba","Ontario","Alberta","British Columbia")
print(canada_provinces)
print("datatype:", type(canada_provinces))

#DICTIONARIES
canadaian_coin = {"nickel": "0.07", "dime": "0.17", "quarter": "0.27"}
print("CAD currency amounts:", canadaian_coin)

print("datatype :", type(canadaian_coin))

canadaian_coin["nickel"] = 7
canadaian_coin["dime"] = 17
canadaian_coin["quarter"] = 27
print(canadaian_coin)

# Adding new items
canadaian_coin["loonie"] = 100
canadaian_coin["toonie"] = 200
print(canadaian_coin)

#SETS
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print("Even number:",even_numbers)
print("datatype:", type(even_numbers))

Multiples_of_5 = {5,10,15,20}
print("Multiples of 5:", Multiples_of_5)

print("difference:",even_numbers.difference(Multiples_of_5))

print("intersection:", even_numbers.intersection(Multiples_of_5))

print(even_numbers.difference(Multiples_of_5))

print(Multiples_of_5.difference(even_numbers))
