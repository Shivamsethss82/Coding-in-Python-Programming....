def median(list1):
    list1.sort()
    num = len(list1)
    if num % 2 == 0:
        med = (list1[num//2 - 1] + list1[num//2]) / 2
    else:
        med = list1[num//2]
    return med

list1 = [4, 2, 3, 2, 4, 5]
print("The median of the list is :",median(list1))