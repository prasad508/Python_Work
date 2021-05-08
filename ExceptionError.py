# Try catch example

n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
try:
    if n1/n2:
        print(n1/n2)

        raise ZeroDivisionError('Devide by zero')
except ZeroDivisionError as msg:
    print("these is error")
