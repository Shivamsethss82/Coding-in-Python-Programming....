'''
Reverse the content of words...
Eg - 
    input = "shivam is king"
    output = "mavihs si gnik"
'''

str1 = "Durga Software solutions"

ls1 = str1.split()
l1 = []
for word in ls1:
    l1.append(word[::-1])
output = ' '.join(l1)
print(output)