class Employee:

    def __init__(self, aname , arole , asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def printdetail(self):
        return f"Name of employee is {self.name}. his role is {self.role} and his salary is {self.salary}"




# If we want to run printdetail() using __init__ constructor

sanket = Employee("Sanket Kulkarni","Engineer",5)
suraj = Employee("Suraj Digi","Sr. Engineer",10 )
guru = Employee("Guru Birajdar","Manager",15 )
praneet = Employee("Praneet Sawant","Director",20 )

# If we want to run printdetail() using self function
"""
sanket = Employee()
suraj = Employee()
guru = Employee()
praneet = Employee()

sanket.name = "Sanket Kulkarni"
sanket.role = "Engineer"
sanket.salary = 5

suraj.name = "Suraj Digi"
suraj.role = "Sr. Engineer"
suraj.salary = 10

guru.name = "Guru Birajdar"
guru.role = "Manager"
guru.salary = 15

praneet.name = "Praneet Sawant"
praneet.role = "Director"
praneet.salary = 20
"""

# Printing employee information
print(sanket.printdetail())