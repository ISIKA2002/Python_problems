#Take positive integer input and tell if it is a four digit number or not.
num=int(input("Enter the number:"))

if num >= 1000 and num <= 9999:
    print("Four digit number")
else:
    print("Not a Four digit number")    