#Typecasting 
#Covert one data type to another data type
a = 2
b = 3
c = 4

a_str= str(a)
b_str= str(b)
c_str= str(c)

final_str= a_str + b_str + c_str
final_int= int(final_str)
print("Final int", final_int, type(final_int))