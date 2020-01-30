# Kathryn Webb
# 1/29/2020
# Write a program which, given the length of three sides of a triangle, will determine whether
# the triangle is right- angled. Assume that the third argument to the function is always the
# longest side. It will return True if the triangle is right-angled, or False otherwise.


sideA = float(input("Measurement of side A:"))
sideB = float(input("Measurement of side B:"))
hyp = float(input("Measurement of the hypotenuse:"))

if (hyp**2) == sideA**2 + sideB**2:
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")
