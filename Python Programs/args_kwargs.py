#Important Python syntax for arguments: first put normal argument then *args and then **args(kw-args)

# Simple function with matching arguments

#def league_of_shadows(a,b,c,d):
#    print("League of Shadows Group: ",a,b,c,d)
    
#league_of_shadows("Sanket","Rahul","Chinmay","Mohit")

# Function arguments do not match the passed arguments

#def league_of_shadows(a,b,c,d):
#   print("League of Shadows Group: ",a,b,c,d)
    
#league_of_shadows("Sanket","Rahul","Chinmay","Mohit", "Sachin")

# Non-keyworded Arguements

#def league_of_shadows1(*args):
#    print("League of Shadows Group Original: ")
#    for i in args:
#        print(i)
        
#members=["Sanket","Rahul","Chinmay","Mohit"]
#league_of_shadows1(*members)

# Normal Arguments

def league_of_shadows1(extend,*args):
    print("League of Shadows Group Extended: ")
    print(extend)
    for i in args:
        print(i)
        
members=["Sanket","Rahul","Chinmay","Mohit"]
extend="Sachin and Anchit"
league_of_shadows1(extend,*members)