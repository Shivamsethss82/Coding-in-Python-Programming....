list1 = [[1,3] , [4,6] , [3,9]]

target_value = 3
replace_value = 7 

for sublist in list1:
    for i in range(len(sublist)):
        if sublist[i] == target_value:
            sublist[i] = replace_value

print(list1)