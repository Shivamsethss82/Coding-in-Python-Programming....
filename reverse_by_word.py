# input = "shivam is king"
# output = "king is shivam"

s = "shivam is king"
l = s.split()

l1 = l[::-1]
output = ''.join(l1)
print(output)