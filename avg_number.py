'''
Take number as a input & Find all the numbers inputs!!!
'''

num = int(input("How many numbers for take input :"))
total_sum = 0
for i in range(num):
    j = i+1
    number = int(input(f"The {j} Number is :"))
    total_sum += number
    avg = total_sum/num
print(total_sum)
print("The Avg of Number : ",avg)


# using the List
num = int(input("How many Numbers: ?"))
l = []
for i in range(num):
    x = int(input())
    l.append(x)
avg = sum(l) / num
print(avg)