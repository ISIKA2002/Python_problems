#create tuple
colours= ("red", "yellow", "green")
'''print (colours)

#create a tuple with 1 item
fruits = ("apple",)
fruits1= tuple("apple")
print (type(fruits))
print (type(fruits1))
print(len(colours))

#accressing items in tuple
print(colours[0]) #positive index
print(colours[-1]) #negative index
print(colours[1:3]) #range index
print(colours[-2:]) #negative range index'''

'''#check item is present or not
if "green" in colours:
    print ("Green is presente")

#traverse the table
for i in colours:
    print(i)'''

'''#concatenate 2 tables
more_colour= ("blue", "brown")
colours= colours + more_colour
print(colours)'''

'''#Unpacking a tuple
colour1, colour2, colour3= colours
print(colour1, colour2, colour3)'''

#reverse a tuple
'''input_tuple=(1,2,3,4,5,6)
print("Before reversed:", input_tuple)
list=[]

for x in reversed(input_tuple):
    list.append(x)

output_tuple= tuple(list)
#output_tuple= input_tuple[::-1]
print("Reverse tuple", output_tuple)'''

#usering user input reverse
'''elements = input("Enter tuple elements separated by space: ")
# convert input string to tuple
tuple_data = tuple(elements.split())

# reverse the tuple
reverse_tuple = tuple_data[::-1] #syntax of silencing

print("Original Tuple:", tuple_data)
print("Reversed Tuple:", reverse_tuple)'''
# USER INPUT WITH PERTIQULAR RANGE AND DO REVERSE
'''n= int(input("Enter the length of tuple:"))
input_tuple=[]

for i in range(n):
    elements= input()
    input_tuple.append(elements)
tuple_data= tuple(input_tuple)
print(tuple_data)
list=[]
for x in reversed(tuple_data):  
    list.append(x)
rev_tuple= tuple(list)
print("Rev data:", rev_tuple)'''


     



