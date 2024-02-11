''' FizzBuzz Problem

If Number div by 3 - Print Fizz
If Number div by 5 - Print Buzz
If Number div by both 3&5 - Print FizzBuzz
Else Return Number Only !!

'''

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 ==0 and i%5 ==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
print(fizzbuzz(50))
