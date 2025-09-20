'''#for loop
for i in range(1, 10):
    print("Hello")'''

'''#print element of a list using for loop
list = [1,2,3,4,5]
for i in list:
    print(i)'''
'''

#While loop   
i= 2
while i< 10:
    print(i)    
    i+= 2 
'''

'''#- Print all even numbers from 1 to 20. 
for i in range (2,21):
    if i % 2 == 0:
     print(i) 
'''
'''#- Iterate through a list of names and print each one.
fruits= ["Mango","Banana","Apple","Strawberry"]
for num in fruits:
    print(num)'''

#- Create a simple login system that asks for a password until the correct one is entered.
correct_password= "admin123@"
psswd= input("Enter password:")
while psswd == correct_password:
    print("Successfully login.")
    break
else:
    print("Invalid!! Try Again.")