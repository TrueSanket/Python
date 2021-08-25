value=True

while (value):
    print("Welcome to Calculator!")
    print("What operation do you want to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit Calculator")

    operation=int(input("Enter the index number: "))

    if operation==1:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print("Sum of two numbers: ",a+b)
    elif operation==2:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print("The subtraction of two numbers is: ",a-b)
    elif operation==3:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print("The multiplication of two numbers is: ",a*b)
    elif operation==4:
        a=int(input("Enter 1st number: "))
        b=int(input("Enter 2nd number: "))
        print("The division of two numbers is: ",a/b)
    elif operation==5:
        break
    else:
        print("Incorrect response")