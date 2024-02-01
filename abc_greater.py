# Write a Python function to find the Max of three numbers. 

print("Using max function :",max(12,1,12))


def max_num(a, b, c):
    max_number = a  # Assume a is the maximum
    
    if b > max_number:
        max_number = b
    if c > max_number:
        max_number = c
    return max_number
# Example usage
print(max_num(12, 1, 12))


# Taking input for three variables
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Calling the function and printing the result
maximum = max_num(a, b, c)
print(f"The greatest number is: {maximum}")

