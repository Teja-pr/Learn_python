# To swap 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Input nos before swapping: "+str(a)+" "+str(b)+" "+str(c))
temp1 = a
a = b
b = temp1
temp2 = b
b = c
c = temp2
print("Input nos after swapping: "+str(a)+" "+str(b)+" "+str(c))