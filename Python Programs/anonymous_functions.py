# Lambda functions or Anonymous functions: Just another method of writing a function
# filter(), map() and reduce() functions

"""def minus (a,b):
    return a-b"""

# Can be written as Lambda/Anonymous function as:

"""minus = lambda a,b: a-b
print(minus(9,4))"""

# Using lambda and filter() functions to filter out even numbers from a given list

"""my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

even_list= list(filter(lambda x: x%2==0, my_list))
print(even_list)"""

# Using lambda and map() functions to double even numbers from even_list

"""even_list = [2, 4, 6, 8, 10, 12]
double_list = list(map(lambda y: y*2, even_list))

print(double_list)"""

# Using lambda and reduce() functions to add all the numbers in double_list

from functools import reduce       # Need to add reduce() function so need to import reduce() from function tools (functools)

double_list = [4, 8, 12, 16, 20, 24]
add_list = reduce(lambda a,b:a+b, double_list)
print(double_list)
print(add_list)