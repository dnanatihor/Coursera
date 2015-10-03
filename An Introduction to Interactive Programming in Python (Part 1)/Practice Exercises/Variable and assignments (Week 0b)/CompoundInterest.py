__author__ = 'rohitanand'

import math

present_value = int(input("Enter amount : "))
annual_rate = int(input("Enter rate : "))
years = int(input("Enter year : "))

print(present_value * ((1 + 0.01 * annual_rate)**years))

