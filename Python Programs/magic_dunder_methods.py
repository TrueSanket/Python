# magic/dunder methods in python: __add__

class employee:
    def __init__(self,fname,lname,salary):  # Using Constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def __add__(self, other):    # defining dunder method/function in class to add salary of 2 objects
        return self.salary + other.salary

    def __repr__(self):
        return ('Employee: {} {} {}'.format(self.fname,self.lname,self.salary))

    def __str__(self):
        return 'The name of the employee is {}'.format(self.fname)

sanket = employee('Sanket','Kulkarni',50000)
guru = employee('Guru','Birajdar',10000)

# check all the dunder methods in Python document https://docs.python.org/3/reference/datamodel.html > 3.3.7 section

a =6
print(a.__add__(7))   # using __add__ dunder method to add 2 numbers

print(a.__mul__(7))   # using __mul__ dunder method to multiply 2 numbers

print (sanket + guru)

print(repr(sanket))

print(sanket)