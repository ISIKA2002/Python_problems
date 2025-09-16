num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
num3=int(input("Enter the num3:"))

#using if- elif
'''
if num1 > num2 and num1 > num3:
  print(f"{num1} is greater")
elif num2 > num1 and num2 > num3:
  print(f"{num2} is greater")
else:
  print(f"{num3} is greater")
'''

#using nested if-else
if num1 > num2:
    if num1 > num3:
        print(num1, "is greater")
    else:
        print(num3, "is greater")
else:   
    if num2 > num3:
        print(num2, "is greater")
    else:
        print(num3, "is greater")