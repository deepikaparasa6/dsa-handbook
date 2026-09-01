def print_items(a,b): #a,b are two different parameters and they are not equal to n
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

print_items(10,5)

''' TIME COMPLEXITY:
- The first loop runs 'a' times, so it's O(a).
- The second loop runs 'b' times, so it's O(b).
- Since both loops are executed sequentially, the overall time complexity is O(a + b).
    WE CANNOT EQUAL A AND B TO N. SO THEY ARE BOTH DIFFERENT PARAMETERS.
'''