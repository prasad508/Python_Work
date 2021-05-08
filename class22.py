#

class Employee:
    def __init__(self):
        self.name = "abc"
        self.login = "@abc1234"
        self.unit = "product"

    def show(self):
        print(self.name,self.login,self.unit)
#encapsulation
    @property
    def emp(self):
        print("getting name")
        return self._emp # private member
    @setattr
    def emp(self , value):
        print("assinging name")
        self._emp = value

# create property object
#emp = property(get_emp, set_emp)

e = Employee()
e.emp = " prasad"
e.show()