num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
def max_two(a,b):
    if a > b:
        max = a
        return max
    elif a < b:
        max = b
        return max
    else:
        max = "equal"
        return max

def max_three(a,b,c):
    if a > b and a > c:
        max = a
        return max
    elif b>c and b >a:
        max = b
        return b
    else:
        max = c
        return max

res3 = max_three(num1,num2,num3)
print("Max of {0}, {1} ,{2} is {3}".format(num1,num2,num3,res3))
res2 = max_two(num1,num2)
print("Max of {0} and {1} is {2}".format(num1,num2,res2))

# using a single line
