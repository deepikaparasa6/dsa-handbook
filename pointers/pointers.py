num1 = 11
num2 = num1 
print("Before updating") 
print("num1:", num1)
print("num2:", num2) 
print("\n num1 points to: ", id(num1))  #where num1 is stored in memory
print("num2 points to: ", id(num2))  #where num2 is stored in memory

#updating num2 to 22
num2 = 22
print("\nAfter updating")
print("num1:", num1)
print("num2:", num2) 
print("\n num1 points to: ", id(num1))  #where num1 is stored in memory
print("num2 points to: ", id(num2))  #where num2 is stored
