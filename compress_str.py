'''
Input :- AAABBBCCC
Output:- A3B3C3
'''

def compress(s):
    n = len(s)
    new_str = ''
    count = 1
    for i in range(0,n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            new_str = new_str + s[i] + str(count)
            count = 1
    new_str = new_str + s[n-1] + str(count)
    return new_str

print(compress("AAABBBCCC"))


# By Using while loop

def compress2(s):
    n = len(s)
    i = 0
    new_str = ''
    while(i<n-1):
        count = 1
        while (i<n-1 and s[i] == s[i+1]):
            count +=1
            i += 1
        i +=1 
        new_str = new_str + s[i-1] + str(count)
    return new_str
print(compress2("AAABBBCCCDD"))