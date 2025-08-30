#Take input percentage of a student and print the Grade according to marks:
#a. 81-100 Very Good
#b. 61-80 Good
#c. 41-60 Average
#d. <=40 Fail
student_p=int(input("Enter the percentage:"))

if student_p >= 81:
    print("Very Good")
elif student_p >= 61: 
    print("Good")
elif student_p >= 41: 
    print("Average")    
else:
    print("Fail")   