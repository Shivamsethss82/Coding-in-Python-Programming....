'''
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def cheaklowupp(str):
    countupp = 0
    countlow = 0
    for i in str:
        if i.isupper():
            countupp += 1
    
        if i.islower():
            countlow += 1
    print("Upper case is :",countupp)
    print("Lower case is :",countlow)

print(cheaklowupp('The quick Brow Fox'))