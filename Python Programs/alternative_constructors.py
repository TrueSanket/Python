# Class methods as Alternative Constructors

class employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    @classmethod     # defining alternative constructor class method to take that object as argument
    def from_str(cls,emp_string):
        fname,lname,salary = emp_string.split("-")
        return cls(fname,lname,salary)

sanket = employee('Sanket','Kulkarni',50000)
suraj = employee('Suraj','Rajamohan',52000)
rohan = employee.from_str("Rohan-Birajdar-60000")      #defining object in alternative way

print(rohan.fname,rohan.lname,rohan.salary)