# Kathryn Webb
# 1/29/2020
# Assume the days of the week are numbered 0 through 6 from Sunday to Saturday.
# Write a program that asks a day number and prints the name (a string).

weekNum = 0
while weekNum != 99:
    weekNum = int(input("What day number?"))
    if weekNum == 0:
        print("Sunday")
    elif weekNum == 1:
        print("Monday")
    elif weekNum == 2:
        print("Tuesday")
    elif weekNum == 3:
        print("Wednesday")
    elif weekNum == 4:
        print("Thursday")
    elif weekNum == 5:
        print("Friday")
    elif weekNum == 6:
        print("Saturday")
    elif weekNum == 99:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again")
