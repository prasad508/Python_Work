# You are given a text, which contains different english letters and punctuation symbols.
# You should find the most frequent letter in the text. The letter returned must be in lower case.
import re

teststr = input("Enter String: ")
teststr=re.sub('[^A-Za-z]+', '', teststr)
c = ''.join(sorted(teststr.lower()))

count = [0] * 256
max = -1
for i in c:
    count[ord(i)] += 1
for i in c:
    if max < count[ord(i)]:
        max = count[ord(i)]
        c = i


print(c.lower())

