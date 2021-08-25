# List comprehension:
# 1. Take an input list from user and print only even numbers
# 2. Do the same with list comprehension

list1=[]
even_list=[]
odd_list=[]

numbers=int(input("How many numbers do you want to add? "))

for i in range(numbers):
    data=input("Enter the numbers: ")
    list1.append(data)
print(list1)

# Print even numbers list

for j in list1:
    if int(j)%2==0:
        even_list.append(j)
    else:
        odd_list.append(j)
print("Even Numbers List: ",even_list)

# Perform same task using list comprehension

even_list1= [k for k in list1 if int(k)%2==0]
print("Even Numbers List by List Comprehension: ",even_list1)