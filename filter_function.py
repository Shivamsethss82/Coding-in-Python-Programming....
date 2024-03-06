def my_filter(predicate, iterable):
    filtered_list = []
    for item in iterable:
        if predicate(item):
            filtered_list.append(item)
    return filtered_list

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = my_filter(lambda x: x % 2 == 0, numbers)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filter numbers greater than 5
greater_than_5 = my_filter(lambda x: x > 5, numbers)
print(greater_than_5)  # Output: [6, 7, 8, 9, 10]
