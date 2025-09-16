eng_marks= int(input("Enter marks in English:"))
math_marks= int(input("Enter marks in Math:"))

if eng_marks > 80 and math_marks > 80:
    print("Grade A")
elif eng_marks > 80 or math_marks > 80:
    print("Grade B")    
else:
    print("Grade C")