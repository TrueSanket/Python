# defining class methods: class methods are special type of methods who takes whole class as an argument
# we need to use decorator for it.
# other functions like below take instance like self as an argument

class employee:

    increment = 2

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def increase(self):
        self.salary = self.salary * self.increment        #using instance variable

    @classmethod     # defining a decorator
    def salary_change(cls, amount):      # giving cls as an argument and amount to increment with that factor
        cls.increment = amount

sanket = employee('Sanket','Kulkarni',50000)
suraj = employee('Suraj','Rajamohan',52000)

print("Sanket's original salary:",sanket.salary)
employee.salary_change(2)
sanket.increase()
print("Sanket's salary after increment:",sanket.salary)

