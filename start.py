# Pattern program
""""
x = input("number of line ")

for x in range(int(x)):

    for i in range(x):
        print(x, end='')
    print('\n')


# second number pattern
lastnumber = 10
for i in range(1,lastnumber):

    for i in range(0, i, 1):
        print(format(2**i, "4d"), end='')
        for i in range(-1+i, -1, -1):
            print(format(2**i, "4d"), end='')
    print(' ')


# heart shape
from turtle import *
import turtle
#turtle.setup(1024, 900)
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('black','red')
width(6)
#print('hello')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()



# printing start full
size = 7
m = (2 * size) -2
for i in range(0, size):
    print("*")
 #   print(" ")                       """

