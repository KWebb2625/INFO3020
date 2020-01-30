# Kathryn Webb
# 1/29/2020
# Write a program which, given the length of two sides of a right-angled triangle, returns the
# length of the hypotenuse

import math

sideA = float(input("Measurement of side A:"))
sideB = float(input("Measurement of side B:"))

hyp = math.sqrt((sideA**2) + (sideB**2))

print("The hypotenuse is ", hyp)
