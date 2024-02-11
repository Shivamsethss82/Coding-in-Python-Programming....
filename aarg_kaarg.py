def example_function(*args, **kwargs):
    # Print positional arguments
    print("Positional arguments:")
    for arg in args:
        print(arg)

    # Print keyword arguments
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage of the function
example_function(1, 2, 3, name="John", age=30 , stanard="5th Class")
