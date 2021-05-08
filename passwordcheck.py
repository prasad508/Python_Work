import re

# check password strength

print("**\n WELCOME TO GMAIL**")
username = input("Enter u r email address:")
password = input("Enter u r password")

if re.search("(?=^.{10,}$)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s)[0-9a-zA-Z!@#$%^&*()]*$", password):
    print('Login Successfully')
else:
    print("Enter strong password")



