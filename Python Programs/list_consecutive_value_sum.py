# sum of the consecutive elements in an input list

# Function to print alternate sum

def pairwiseSum(lst, n):
	sum = 0;
	for i in range(len(lst)-1):
		
		# adding the alternate numbers
		sum = lst[i] + lst[i + 1]
		print (sum, end = " ")
	
# driver function to test function
arr =[4, 10, 15, 5, 6]
print(arr)

#arr=[]
#number=input("Enter number of elements you want in the list: ")
#for i in number:
#    data=input("Enter the numbers: ")
#    arr.append(data)

size = len(arr)
pairwiseSum(arr, size)
