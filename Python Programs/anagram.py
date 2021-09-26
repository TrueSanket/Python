str1 = input(str("Enter a string: "))
str2 = input(str("Enter another string: "))

# convert both the strings into lowercase
str11 = str1.casefold()
str22 = str2.casefold()

# check if length is same
if(len(str11) == len(str22)):

    # sort the strings
    sorted_str1 = sorted(str11)
    sorted_str2 = sorted(str22)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")