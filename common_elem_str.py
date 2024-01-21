'''
Write Program to find out to common letters between two string ?
eg = 
1) NAINA
2) REENA

'''

def common_letter():
    str1 = input("Enter first string: ")
    str2 = input("Enter Secound string: ")
    s1 = set(str1)
    s2 = set(str2)
    lst = s1 & s2
    return lst
print(common_letter())