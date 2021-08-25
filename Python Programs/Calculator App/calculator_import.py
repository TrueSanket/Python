import addition
import divide
import multiply
import subtraction

print("Welcome to Calculator!")
print("What operation do you want to perform?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation=input("Enter number: ")

if operation==1:
    sum()
elif operation==2:
    subtract()
elif operation==3:
    multiply()
elif operation==4:
    divide()
else:
    ("Incorrect response")