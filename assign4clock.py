# clock conversion program
import time
p = input("Enter Time :")
[hours,mins]=p.split(':')
hours=int(hours)
ampm='am'
if hours>12:
    hours=hours-12
    ampm = 'pm'
    if hours==0:
        hours=12
print(str(hours)+':'+mins+' '+ampm)

