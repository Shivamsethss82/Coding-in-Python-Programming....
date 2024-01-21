arr = [1,3,2,3,4,5,6,7,7,8,2,3,5,5,4,2,4,4]

# Using Set
arr1 = list(set(arr))
print(arr1)


# without using set
arr2 = []
for i in arr:
    if i not in arr2:
        arr2.append(i)
print(arr2)


# Using lamda function
rem_dup_func = lambda arr:set(arr)
print(rem_dup_func(arr))


# Using dictionary
dict1 = {
    'car' : ["Toyata", "ford","Toyata", "ford","Toyata", "ford"],
    'barnd' : ["mustang", "wolkwagon","mustang", "wolkwagon","mustang", "wolkwagon"]
}
dict2 = {}
for key , value in dict1.items():
    dict2[key] = set(value)
print(dict2)


# Using semetric difference - Remove duplicate values

set1 = {1,2,4,5}
set2 = {2,1,5,7}
rem_dup_elem = set1.symmetric_difference(set2)
print(rem_dup_elem)