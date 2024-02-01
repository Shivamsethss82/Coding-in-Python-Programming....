# recursive Methods:
def fact(n):
    if n == 1:
        return 1
    return (n* fact(n-1))
print(fact(5))



# iterative Methods:
def factorial(num):
    prod = 1
    for i in range(num):
        prod = prod * (i+1)
    return prod
print("The fact is: ",factorial(5))