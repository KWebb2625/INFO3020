# Kathryn Webb
# 1/29/2020
# Assume you have the assignment numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (a) Write a loop that adds all the numbers from the list into a variable called total. You
# should set the total variable to have the value 0 before you start adding them up, and print the
# value in total after the loop has completed.
# (b)  Print the product of all the numbers in the list. (product means all multiplied together)

total = 0

for num in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    total += num

print("The total is ", total)

total = 1
for num in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    total *= num
print("The product is ", total)

