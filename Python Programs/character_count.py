## Take a name or sentence from a user and then take a character from user. Using for/while loop search the name/sentence for that characterand print "number of times" that character appeared in that name/sentence##


counter = 0
ip_string=str(input("Enter a name or sentence: "))
character=input("Enter a character that you wish to count in it: ")
ip_string1=ip_string.casefold()   # neutralizes all the uppercase letters in the input

# Using basic method of incrementing counter

for i in ip_string1:
    if i == character:
        counter = counter + 1
  
print ("That character appears "+ str(counter) + " times")

# Using count() method

counter = ip_string1.count(character)

print ("That character appears "+ str(counter) + " times")