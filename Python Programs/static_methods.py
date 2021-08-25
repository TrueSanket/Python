# Using static method if we don't want to use class or instance variables
# That is, if we want a function who does not take class or instance variables as an argument

class employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    @classmethod     # defining a decorator
    def salary_change(cls, amount):      # giving cls as an argument and amount to increment with that factor
        cls.increment = amount

    @classmethod  # defining alternative constructor class method to take that object as argument
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod   # static method/function decorator
    def weekend(day):
        if day == 'sunday':
            return True
        else:
            return False

print(employee.weekend('sunday'))
