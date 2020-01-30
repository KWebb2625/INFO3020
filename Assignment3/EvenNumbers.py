# Kathryn Webb
# 1/29/2020
# Write a program that counts the number of even digits in the scope of 1-1000

totalCount = 0
for num in range(1, 1000):
    if num%2 == 0:
        totalCount += 1

print("There are", totalCount, "even numbers between 1 and 1000")
