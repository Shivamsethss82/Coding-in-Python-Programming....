
list1 = [1,4,4,5]
for i in list1:
    if i == 4:
        list1.remove(i)
print(list1)
# Output :- [1, 4, 5]



list1 = [1, 2, 2, 5]
while 2 in list1:
    list1.remove(2)
print(list1)
# Output :- [1, 5]
