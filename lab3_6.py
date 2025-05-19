my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp_list = []

for num in my_list:
    if num not in temp_list:
        temp_list.append(num)

print("The list with unique elements only:")
print(temp_list)

