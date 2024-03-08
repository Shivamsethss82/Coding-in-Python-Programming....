def calculate_contribution(string, values, length):
    if len(string) < length:
        return sum(values)
    else:
        sorted_values = sorted(values)[:length]
        return sum(sorted_values)

string1 = "cccbb"
values1 = [3, 3, 3, 2, 2]
print(calculate_contribution(string1, values1, 6))  # Output: 13

string2 = "bdbbabdb"
values2 = [2, 4, 2, 2, 1, 2, 4, 2]
print(calculate_contribution(string2, values2, 6))  # Output: 11

strings = ["baceabad", "baceabad", "baceabad"]
values3 = [[1, 1, 2, 2, 2, 5], [1, 1, 1, 2, 2, 3], [1, 1, 1, 1, 1, 4]]
total_contribution = sum(calculate_contribution(strings[i], values3[i], 6) for i in range(len(strings)))
print(total_contribution)  # Output: 32
