#  Inheriting all the methods of a class into a new class

class employee:
    def __init__(self,fname,lname,salary):  # Using Constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary

sanket = employee('Sanket','Kulkarni',50000)
suraj = employee('Suraj','Rajamohan',60000)

class employee2(employee):

    print("Now, inheriting methods from employee class into employee2 class")

    print("Employee " + sanket.fname + " " + sanket.lname + " with salary", sanket.salary)
    print("Employee " + suraj.fname + " " + suraj.lname + " with salary", suraj.salary)

    if sanket.salary < suraj.salary:
        print("Suraj's salary is more")
    else:
        print("Sanket's salary is more")