list1 = [1,2,3,4,5,6,7,8,9]
def print_even(list1):
    list2 = []
    for i in list1:
        if i%2==0:
            list2.append(i)
    return list2

print(print_even(list1))


# Odd Even Without Mod

num = int(input("Enter the Number ?"))
def isEven(num):
    return num&1
if isEven(num) == 0:
    print(f'Number {num} is Even')
else:
    print(f'Number {num} is Odd')