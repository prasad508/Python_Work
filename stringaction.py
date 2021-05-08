# diffrent string opration
"""
string = 'Happy New year 2019'

print('\n first letter caps:\t', string.capitalize())

print('\n all caps:\t', string.upper())

print('\n all lower:\t', string.lower())

print('\n join:\t', string.join('$$'))

print('\n all caps:\t', string.rjust(24, '@'))

print('\n all caps:\t', string.replace('a', '@'))




# String operation.

def revs(s):
    str = ""
    for i in s:
        str = i + str
        return str
    s = 'Indian Army!'
    print("original string is: ", end="")
    print(s)
    print("Reverse string is: ", end="")
    print(revs(s))
"""

# Multiple inputs

ram, shyam = input("Enter ages:  ").split()
print("ram age is:", ram)
print("shyam age is:", shyam)