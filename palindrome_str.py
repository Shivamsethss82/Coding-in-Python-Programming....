# Palindrome Number 
# By split methods -- Best Approach


def palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("Yes it is a palindrome Number !")
    else:
        print("Not its not a palindrome Number !")

s = "nitinn"
palindrome(s)

# By using indexing or using for loop

def palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True
print(palindrome2("naman"))


# By using inbuilt function - reverse and join

def palindrome3(s):
    # rev_st = reversed(s)
    # for i in rev_st:
    #     print(i)
    temp = ''.join(reversed(s))
    if temp == s:
        return True
    else:
        return False
    # print(rev_st)

print(palindrome3("naman1"))

# Using while loop

def palindrome4(s):
    n = len(s)
    first = 0
    last = n-1
    while(first < last):
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True
        
print(palindrome4("12111"))