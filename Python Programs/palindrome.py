#palidrome

decision=input("What do you want to test for Palindrome? ('n' for a Number or 's' for a String): ")

if decision== "Number" or "String":

    if decision=="n":
        num=int(input("Enter a number:"))
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print("The number is palindrome!")
        else:
            print("Not a palindrome!")

    elif decision=="s":
        string=input(("Enter a string:"))
        string1=string.casefold()               #Important: Casefold function neutralizes the case-sensitive words of the input
        if(string1==string1[::-1]):
            print("The string is a palindrome")
        else:
            print("Not a palindrome")
else:
    print("Input entered was invalid")