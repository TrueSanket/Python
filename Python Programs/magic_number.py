#1. Define any magic number in the program
#2. Take a "number" as an input from the user
#3. If user entered same number = Congrats! guessed number higher then print "higher" if guessed lower then print "lower"

number= 13
print("Welcome to the number guessing game!!")
guess=int(input("Enter a number between 1 to 25: "))

while guess!=number:
    if guess>number:
        print("The number is smaller than your guess, try again!")
        guess=int(input("Enter a number between 1 to 25: "))
    else:
        print("The number is greater than your guess, try again!")
        guess=int(input("Enter a number between 1 to 25: "))
print("Congratulations!! You have guessed the number correctly!")