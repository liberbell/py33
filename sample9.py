list_a = [1, 2, 3]
all_list = [list_a, list_a, list_a]
print(all_list)

list_a.append(4)
print(all_list)

all_list[0].append(5)
print(all_list)

all_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(all_list)
all_list[0].append(4)
print(all_list)

list_a = [1, 2, 3]
all_list = [list_a.copy(), list_a.copy(), list_a.copy()]
print(all_list)

all_list[0].append(4)
print(all_list)