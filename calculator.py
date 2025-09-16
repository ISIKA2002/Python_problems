#Match cash
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
operator=input("Enter the operator:")

match operator:
    case "+":
        print("Sum=", num1 + num2)
    case "-":
        print("Substraction=", num1 - num2)
    case "*":
        print("Multiple=", num1 * num2)   
    case "/":
        print("Devision=", num1 / num2)     
    case _:
        print("Enter a valid operater")    