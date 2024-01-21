# Max and min value without using min and max function

def max_num_arr(arr):
    max = arr[0]
    size = len(arr)
    for i in range(size):
        if arr[i] > max:
            max = arr[i]
    return max


def min_val_of_arr(arr):
    min = arr[0]
    size = len(arr)
    for i in range(size):
        if arr[i] < min:
            min = arr[i]
    return min

arr = [1,9,3,4,5,11,6,7,8]
print("The maximum value of array is :",max_num_arr(arr))
print("The manimum value of array is :",min_val_of_arr(arr))