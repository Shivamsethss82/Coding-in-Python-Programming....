# Using the flag

def prime_number(n):
    flag = False
    if n>1:
        for i in range(2,(n//2+1)):
            if n%i ==0:
                flag = True
                break
    if flag:
        return "No! Its not a Prime Number "
    else:
        return "Yes! Its is a Prime Number "
print(prime_number(7))


# Using for-else
def prime_number2(n):
    if n>1:
        for i in range(2, n//2+1):
            if n%i ==0:
                print("No! Its not a Prime Number")
                break
        else:
            print("Yes! Its is a Prime Number")
print(prime_number2(9))

# Display a range of prime number :-

def prime_number_all(start,end):
    for n in range(start, end):
        if n>1:
            for i in range(2, n//2+1):
                if n%i ==0:
                    break
            else:
                print(n)
prime_number_all(1,100)