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
print("Odd Numbers List: ",odd_list)