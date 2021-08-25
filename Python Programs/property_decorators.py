class employee:

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        #self.email= fname + '.' + lname + '@gmail.com'

    def email(self):   # declaring method/function for email instead of writing it as an instance in self
        return self.fname + '.' + self.lname + '@gmail.com'

if __name__== '__main__':
    sanket = employee('Sanket', 'Kulkarni', 50000)
    suraj = employee('Suraj', 'Rajamohan', 52000)

    print(sanket.email())
    print(suraj.email())
    suraj.lname= 'Kumar'   #changing parameter of existing object
    print(suraj.email())