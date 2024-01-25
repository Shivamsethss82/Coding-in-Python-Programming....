num = [1,2,3,4,5,6,7,8]

def sqr(x):
    return x**2

# Using Map function

sqrt = map(sqr,num)
output = list(sqrt)
print(output)

def odd_even_check(y):
    if y%2 == 0:
        return True
    else:
        return False

# Use filter function

check = filter(odd_even_check, num)
list1 = []
for i in check:
    list1.append(i)
print(list1)
    