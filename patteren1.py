'''#print *****
n = int(input("Enter n:"))
for _ in range(n):
    print("*" * 5)'''

'''#print for n=4 
1234
1234
1234
1234

r = int(input("Enter r:"))
for i in range(r):
   for j in range(1, r+1):
     print(j, end="")
   print()'''

'''#print for n=4 
1
12
123
1234

n = int(input("Enter n:"))
for i in range(1, n+1):
   for j in range(1,i+1):
     print(j, end="")
   print() '''

'''#print for n=4 
A
AB
ABC
ABCD

n = int(input("Enter n:"))
for i in range(1, n+1):
   for j in range(65, 65 + i): 
     print(chr(j), end="")
   print()'''
'''#print for n=4 
   1
  123
 12345
1234567'''
n = int(input("Enter n:"))
for i in range(1, n+1):
   print(" " * (n-i), end="")
   for j in range(1, 2 * i): 
     print(j, end="")
   print()