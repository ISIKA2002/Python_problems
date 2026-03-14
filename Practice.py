'''n= int(input("Enter n:"))

for i in range(n):
    print("*" * 5)'''

'''n= int(input("Enter coloumn and row:"))
for i in range(n):
    for q in range(1, n+1):
        print(q, end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(1, n+1):
    for q in range(1, i+1):
        print(q, end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(n, 0, -1):
    for q in range(1, i+1):
        print(q, end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(1, n+1):
    for q in range(i):
        print(chr(65+q), end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(n, 0, -1):
    for q in range(i):
        print(chr(65+q), end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(1, n-i):
    for q in range(i):
        print(q, end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for q in range(1, (2*i)):
        print(q, end="")
    print()'''

'''n= int(input("Enter coloumn and row:"))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for q in range(1, 2*(n-i)):
        print(q, end="")
    print()'''

