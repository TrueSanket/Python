# There are three types of errors - SyntaxError, LogicalError and RuntimeError and 'Exception' is an umbrella error which handles all of them and other errors which system may encounter

print("Starting the code")
a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))

# Without error handling

"""c = a/b
print("Division: ",c)
print("That was smooth")"""

# With error handling - exception handling with pass

"""try:
    c = a / b                                    # Critical Statement(means: not sure if this will run or not)
    print("Division: ",c)
except Exception as e:                           # if critical statement fails, don't end the program here, proceed with rest of the lines!
    print("There is an error, system says: ",e)
finally:
    print("Finishing up the code")"""

# With error handling - exception handling with pass - Don't want to show except error

"""try:
    c = a / b                                    
    print("Division: ",c)
except ZeroDivisionError:                        
    print("You cannot divide a number by zero")
    pass                                      # writing pass means it will not show the exception and proceed to next lines"""

# With error handling - exception handling with finally

"""try:
    c = a / b                         
    print("Division: ",c)
except ZeroDivisionError as e:        
    print("You cannot divide a number by zero, system generated error message: ",e)
finally:
    print("Finishing up the code")"""

# Error handling with multiple exceptions and finally - NEED TO COMMENT OUT 1st THREE LINES ABOVE

"""print("Starting the code")
a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))

try:
    c = a / b
    print("Division: ",c)
    k= int(input("Enter another number to print: "))
    print(k)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero, system generated error says: ",e)
except ValueError as e:
    print("Invalid input. You were asked to enter a number, system generated error says: ",e)
except Exception as e:
    print(e)
finally:
    print("Finishing up the code")"""

# Error handling with exception and else statement

"""try:
    c = a / b
    print("Division: ",c)
except Exception as e:
    print("There is an error, system says: ",e)
else:
    print("System gave error for the intended operation")
    print("Let's multiply and see what's output: ",(a*b))
    print("If it was zero, then you have entered denominator value as zero")
finally:
    print("Finishing up code")"""