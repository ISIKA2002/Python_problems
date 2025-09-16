#question
n=int(input("Enter the number:"))
 
if n % 15 == 0:
    print(n,"is divisible by 15")
else:
    if n % 3 == 0 or n % 5 == 0:
      print("Numbers are not devisible by 15 but divisible by 3 and 5.")
    else:
       print("Number is neither divisible 3 and 5.")     