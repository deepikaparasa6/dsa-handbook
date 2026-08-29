def print_items(n):
    for i in range(n):
        print(i)
print_items(10)

# the time complexity is O(n) because the function iterates through a loop n times, 
# printing each number from 0 to n-1.

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)
#the time complexity is O(n) because the function iterates through two separate loops, 
# each running n times. The total number of iterations is 2n, which simplifies to O(n).
# basically called as drop constants -> n + n = 2n -> O(n) (dropped constant)
