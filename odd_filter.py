def odd(x):
    return (x %2 ==1)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
result = filter(odd, a)
print(list(result))


# Odd Index element filter in the list :-

list1 = [1,2,3,4,5]
print(list1[1::2])
#or
result = [list1[i] for i in range(len(list1)) if i % 2 != 0]
print(result)
