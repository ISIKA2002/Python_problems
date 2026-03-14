#list types
Fruits=["Mango", "Banana", "Apple", "Kiwi"]
'''print(Fruits)
print(type(Fruits))
print(len(Fruits))

#check a item is present in the list
if "Banana" in Fruits :
 print("Banana is present") 

#check a item is not present in the list
if "Kiwi" not in Fruits :
 print("Kiwi is not present")

#Accessing items of a list
#check index 
print(Fruits[2])
print(Fruits[-1])

print(Fruits[1:2])
print(Fruits[-2:-1])'''

'''#Adding elements to the list
#append()
Fruits.append("orange")
print("append function:", Fruits)

#insert()
Fruits.insert(2, "Pineapple")
print("insert function:", Fruits)

#extend()
Fruits1=["Papaya", "Mango"]
Fruits.extend(Fruits1)
print("extend function:", Fruits)'''

'''#Removing elemets from a list
#remove()
Fruits.remove("Apple")
print("remove function:", Fruits)

#pop()
Fruits.pop(1)
print("pop function1:", Fruits)
#or
Fruits.pop() #it remove the last index item
print("pop function2:", Fruits)'''

'''#Change items in list or updating in a list
#At an index
Fruits[1]= "Watermelan"
print(Fruits)

#In a range
Fruits[1:3]= ["Pineapple"]
print(Fruits)'''

'''
#shorting a list
# Fruits.sort() #by defult ascending order
print(Fruits)
Fruits.sort(reverse=True) #descending
print(Fruits)
Fruits.reverse()
print(Fruits)'''

#list comprehension
new_Fruits=[Fruits for Fruits in Fruits if "a" in Fruits]
print(new_Fruits)
