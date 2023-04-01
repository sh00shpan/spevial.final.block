
list_check = ["hello", "world", "123", "py", "geekbrains", "gb"]

list_result = []

for i in list_check:
    if len(i) <= 3:
        list_result.append(i)

print(list_result)