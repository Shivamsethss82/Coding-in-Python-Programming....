# Print first 10 Fibonachi Number using Recursion

def recur(n):
    if n<=1:
        return n
    else:
        return (recur(n-1) + recur(n-2))
    
n = 10
for i in range(n):
    print(recur(i))