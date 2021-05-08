"""
#weekday = False       #global declaration
#vacation = False

def sleeping(weekday,vacation):
    if not weekday or vacation :
#        print(" you can sleep") # function not print it return value
        return True
    else:
#        print("work time")
         return False

# calling function
sta = sleeping(True, False)
if sta:
    print("sleep")
else:
    print("zombie")         """

# calculator
def cal(**args):
    print(args)
    print(args['option'])
    for a in args:
        print(a)

def cal1(*args, **args1):   #default para
    str= " "
def cal2(option,data):
    str1 = " "
    print(data,option)
