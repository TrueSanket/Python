# Object Orriented Programming - Class and Object


class Computer:
    
    def config(self):
        print("Configuration = Intel i5 processor, 4GB RAM and 1TB HDD")


comp1 = Computer()
comp2 = Computer()

# One way of calling the object

Computer.config(comp1)
Computer.config(comp2)

# Another way of calling object - explains 'self' defined in Class = self is an object which you are passing

comp1.config()
comp2.config()
