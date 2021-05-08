# interrogating with system
import sys, keyword
from datetime import*


print('python version:', sys.version)

print('Interpretor loaction:', sys.executable)

print('python module search PATH:')

for dir in sys.path:
    print(dir)

    print('keyword list:')

    for word in keyword.kwlist:
        print(word)

print("Today is:", datetime.today())

for att in \
        ['YAER', 'MONTH', 'DAY', 'HOUR','MINUTE', 'SECOND','MICROSECOND']:
    print(att)


