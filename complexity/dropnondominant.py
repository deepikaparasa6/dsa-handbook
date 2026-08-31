def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
print_items(10)
''' here the time complexity is O(n^2) because the 
function contains a nested loop that iterates n times 
for each iteration of the outer loop, resulting in n * n = n^2 iterations. 
The second loop runs n times, but it does not change 
the overall time complexity since O(n^2) dominates O(n). 
Therefore, the total time complexity is O(n^2).'''

''' O(n^2 + n) -> O(n^2) (dropped non-dominant term)'''