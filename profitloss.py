'''If cost price and selling price of an item is input through the keyboard,
write a program to determine whether the seller has made profit or incurred
loss or no profit no loss. Also determine how much profit he made or loss he
incurred.'''

#if else considition statement

'''
cost_p= int(input("Enter cost price:"))
selling_p=int(input("Enter selling price:"))

if selling_p > cost_p:
    profit= selling_p - cost_p
    print ("We have made the profit of", profit)
else :
    loss = cost_p - selling_p
    print ("We have incurred loss of", loss)
'''    
#elif conditional statement
cost_p= int(input("Enter cost price:"))
selling_p=int(input("Enter selling price:"))

if selling_p > cost_p:
    profit= selling_p - cost_p
    print ("We have made the profit of", profit)
elif selling_p < cost_p:
    loss = cost_p - selling_p
    print ("We have incurred loss of", loss)
else:
    print("We have made  no profit and no loss.")    