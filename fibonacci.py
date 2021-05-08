# Fibonacci series number
num = int(input("Enter how many terms you want:"))
n1 = 0
n2 = 1

# check for valid no

if num < 0:
    print("Enter positive no")
elif num <= 1:
    print("Fibonacci of series:", num)
    print(n1)
elif num >= 2:
    print("{}, {}:".format(n1, n2), end='')
for i in range(2, num):

        num = n1+n2
        print(", {}".format(num), end='')
        n1 = n2
        n2 = num



