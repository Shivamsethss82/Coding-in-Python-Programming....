def generate_values_from_pattern(string):
    pattern = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            pattern.extend([count] * count)
            count = 1
    pattern.extend([count] * count)
    return pattern

string1 = "eaaadada"
values1 = generate_values_from_pattern(string1)
print(sum(values1))
