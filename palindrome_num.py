# Using Wlile loop:- Best Approach

def palindrome(n):
    temp = n
    rev_num = 0
    while(temp > 0):
        digit = temp % 10
        # print(digit)
        rev_num = rev_num * 10 + digit
        temp = temp // 10
    if n == rev_num:
        return True
    else:
        return False
    

# Worst Approach 

def palindrome1(n):
    s = str(n)
    temp = s[::-1]
    if s == temp:
        print("Yes it is a palindrome Number !")
    else:
        print("Not its not a palindrome Number !")

n = 12521
print(palindrome(n))
print(palindrome1(n))


