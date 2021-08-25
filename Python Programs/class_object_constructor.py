# Creating class, objects and constructors.
# Self is the first argument to be passed in Constructor and Instance Method.
# Self must be provided as a First parameter to the Instance method and constructor.

class employee:
    def __init__(self,fname,lname,salary):  # Using Constructor
        self.fname=fname
        self.lname=lname
        self.salary=salary

sanket = employee('Sanket','Kulkarni',50000)
suraj = employee('Suraj','Rajamohan',52000)

# Passing arguments to objects created above
"""sanket.fname = 'Sanket'
sanket.lname = 'Kulkarni'
sanket.salary = 50000

suraj.fname = 'Suraj'
suraj.lname = 'Rajamohan'
suraj.salary = 52000 """

print(sanket)
print(suraj)

print("Employee "+sanket.fname+" "+sanket.lname+" with salary",sanket.salary)
print("Employee "+suraj.fname+" "+suraj.lname+" with salary",suraj.salary)

if sanket.salary < suraj.salary:
    print("Suraj's salary is more")
else:
    print("Sanket's salary is more")