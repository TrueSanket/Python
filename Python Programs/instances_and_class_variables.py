# understanding instances and class variables

class employee:
    increment = 1.5  # defining class variable

    def __init__(self,fname,lname,salary):  # Using Constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment= 2   # defining instance variable

    def increase(self):
        #self.salary = self.salary * employee.increment    # using the class variable
        self.salary = self.salary * self.increment        #using instance variable

# If used self.increment, python will 1st search for it in __init__ function but since employee.increment is used,
# it searched for increment variable in employee class

sanket = employee('Sanket','Kulkarni',50000)
suraj = employee('Suraj','Rajamohan',52000)

print("Employee "+sanket.fname+" "+sanket.lname+" with salary",sanket.salary)
# print(suraj.__dict__)   # prints all the variables declared in that instance self
sanket.increase()
print("Sanket's salary after increment: ",sanket.salary)