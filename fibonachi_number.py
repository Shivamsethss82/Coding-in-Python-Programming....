# Fibonacci function using recursion
def fibonachi(n):
    if n <= 0:
        return n
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

# Printing first 10 Fibonacci numbers using recursion
n = 10
for i in range(n):
    print(fibonachi(i))



# Fibonacci function using while loop
def fibo(n):
    a, b = 0, 1
    while b <= n:
        print(b)
        a, b = b, a + b
    return

print(fibo(n))



# Fibonacci function using for loop
def fibo2(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
    return

print(fibo2(n))