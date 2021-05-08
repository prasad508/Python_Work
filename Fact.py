# Factorial  program

"""fact = 1
num = int(input("Enter No for Factorial: "))

if num < 0:
    print("sorry no factorial for negative number")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact*i
        print("Factorial of ", num, "is", fact)
"""

# Factorial  program using recursion


def re_fact(n):
    if n == 1:
        return n
    else:
        return n*re_fact(n-1)


num = int(input("Enter No for Factorial: "))

if num < 0:
    print("sorry no factorial for negative number")
elif num == 0:
    print("The Factorial of 0 is 1")
else:

        print("Factorial of ", num, "is", re_fact(num))


