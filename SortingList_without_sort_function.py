data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

while data_list:
    minimum = data_list[0]
    for i in data_list:
        if i < minimum:
            minimum = i
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)