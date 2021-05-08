# Tupple

"""
x = [33,44,77]
y = [23,45,66]

import matplotlib.pyplot as pt

pt.plot(x,y)
pt.show()


a = 23
b = (23,)

print(a,b)
print(type(a), type(b))

lis = [1,2,4,5]
tup = (1,2,4,5)
lis [2]= 3
print(lis)

#tup [2] = 3    cant add immutable

lis.insert(3,"p")
print(lis)

x = [1,2]
y = [5,7,2]

z = x+y # multiple value
print(z)

p = (1,2)
q = (5,7,2)

p = p+q # overide
print(p)

print(len(q))

# check palindrom

tstr = ('dad',)
#print(tstr)

l= len(tstr)
i = 0
flag = False

for i in range(0, l//2,1):
    first = str[i]
    last = str[l-1]
    if first == last:
        flag = True
    else:
        flag = False
        break
        print(" ")
    if flag :
        print("palindrom")
    else:
        print("NA")    """


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

