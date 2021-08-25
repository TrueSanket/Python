"""
File Handling - File IO Basics

"r" = Open file for reading - default mode
"w" = Open file for writing
"x" = Creates file if it doesn't exist
"a" = Add more content to a file
"t" = text mode - default mode
"b" = binary mode
"+" = read and write
"""

# Reading the file

"""x = open("tmux_read.txt")
content = x.read()
print(content)
x.close()"""

# Reading the file

"""x = open("tmux_read.txt","r")       # reading mode which is by default
content = x.read()
print(content)
x.close()"""

# Reading the file in text mode

"""x = open("tmux_read.txt","rt")       # reading in text mode which is by default
content = x.read()
print(content)
x.close()"""

#Reading file in binary mode

"""x = open("tmux_read.txt", "rb")       # reading in binary form
content = x.read()
print(content)
x.close()"""

# Reading only specified number of characters in the file in text mode

"""x = open("tmux_read.txt","rt")

content = x.read(10)              # read 1st 10 characters
print(content)

content = x.read(10)              # read next 10 characters
print(content)

x.close()"""

# Adding to the print while reading content in the file in text mode

"""x = open("tmux_read.txt","rt")

content = x.read()
print("Contents of the file are: ",content)

x.close()"""

# Reading text file character by character in new lines

"""x = open("tmux_read.txt","rt")
content = x.read()

for y in content:
    print(y)

x.close()"""

# Reading text file line by line in new lines with readline() function

"""x = open("tmux_read.txt","rt")

print(x.readline())
print(x.readline())
print(x.readline())
print(x.readline())    # text ends here but if you still use readline(), it will just but a blank line
print(x.readline())    

x.close()"""

# Reading text file as a list with readlines() function

x = open("tmux_read.txt","rt")
print(x.readlines())
x.close()