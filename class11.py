# character list occurance
"""
word = 'prasad'

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(2,26):
    print(alpha[i], ":", word.count(alpha[i]))


# 2nd way
from collections import  Counter  #explicet import

counts = Counter(word.lower())
for j in word:
    print(j, counts[j])
"""

dict = {}  #dictionary
list = [] #list

#dict1 = {'name':"prasad","age":27}
#print(dict1)

alpha = {"name":"alpa", "age":24,"rajit":" male"}
for rajit in alpha:
    print(" ")
if rajit in alpha:
    print("matched")
else:
    print("she don't like")

print(alpha)

