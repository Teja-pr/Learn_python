num = int(input("Enter the number: "))

def factorial(num):
    res = 1
    for i in range(1,num+1):
        res = res * i
    return res

res = factorial(num)
print("Factorial of {0} is {1}".format(num,res))



