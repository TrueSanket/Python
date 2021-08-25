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

#Writing to the file (Creates if doesn't exist) txt format file

"""x = open("tmux_write.txt","w")
content=x.write("Instructions to open tmux")
x.close()"""

#Writing to the file (Creates if doesn't exist) odt format file

"""x = open("tmux_write.odt","w")
content=x.write("Instructions to open tmux")
x.close()"""

# Append contents to the file

"""x = open("tmux_write.txt","a")
content=x.write("\nFollowing are the instructions on how to open tmux terminal:\n")
x.close()"""

# Print how many characters are written to the file

"""x = open("tmux_write.txt","w")
content=x.write("\nFollowing are the instructions on how to open tmux terminal:\n")
print(content)
x.close()"""

# Handle read and write both

x = open("tmux_write.txt","r+")
content=x.write("\nInstructions to open tmux")
x.write("\nCompleted")
x.close()