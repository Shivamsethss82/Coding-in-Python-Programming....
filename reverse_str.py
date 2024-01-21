## Reverse a string

name = 'shivam'
print(name[::-1])


## Through a reverse function
s = 'ram'
l = reversed(s)
res = ''.join(l)
print(res)


## without using reverse function or sclicing

a = "kamal"
output = ''
i = len(a) -1
while i>=0:
    output = output + a[i]
    i = i-1
print(output)