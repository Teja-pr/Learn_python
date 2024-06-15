# To determine the given input number is odd or even number
x = input("Enter the number: ")
if int(x) == 0:
    print(str(x) + " is zero number")
elif int(x)%2 == 0:
    print(str(x)+" is even number")
elif int(x)%2 == 1:
    print(str(x)+" is odd number")
else:
    print(str(x)+" is negative number")