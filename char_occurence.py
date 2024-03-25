# Character Occourance 
# 1 Least Repeating char

def least_char_occourence(s):
    print(s)
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch)
    result = min(ch, key = ch.get)
    print("The min occourance char is :",result)
s = "aaaaajdggiidd"
print(least_char_occourence(s))


# Using Inbuilt function counter
from collections import Counter
s = "aaaaajdggiidd"
ch = Counter(s)
res = max(ch, key=ch.get)
print("The max occous char is :",res)


# 2 Count any perticular element
# Without using count function:-
def count_char_occourence(s, search_ch):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch)
    try:
        print(ch[search_ch])
    except:
        print(0)
s = "aaaaaaajdggiidd"
print(count_char_occourence(s, 'a'))

# Using count function:-
l1 = [1,2,3,4,4,4,4,1,1,3]
print(l1.count(2))
print(l1.count(4))


# 3 Count of all elements

def all_char_occourence(s):
    print(s)
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch)
print(all_char_occourence("aaaaaaajdggiidd"))


# Perticular Charecter count

days = ['S','M','M','M','F','S']
y = set(days)
print([[x,days.count(x)] for x in y])
