#1. Define any magic number in the program
#2. Take a "number" as an input from the user
#3. Give only 5 chances for user to guess the number correct
#4. If user entered same number = Congrats! guessed number higher then print "higher" if guessed lower then print "lower"

number=8
count=1

print("Welcome to the number guessing game!!")
print("You only have 5 chances to guess the number correctly")
guess=int(input("Enter a number between 1 to 15: "))

while guess!=number:
    count=count+1
    if count>5:
        print("Sorry, you are have reached maximum guesses, try again later!")
        break
    else:
        if guess>number:
            print("The number is smaller than your guess, try again!")
        else:
            print("The number is greater than your guess, try again!")
    guess=int(input("Enter a number between 1 to 15: "))
    print("Congratulations!! You have guessed the number correctly!")