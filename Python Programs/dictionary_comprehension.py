dict1= {i:f"item {i}" for i in range(0,11)}
print("All items 0 to 10=",dict1)

dict2= {j:f"item {j}" for j in range(0,11) if j%2==0}
print("Even items from 0 to 10=",dict2)