my_list = input('Список через запятую: ')
my_list = my_list.split(',')

for i in range(1, len(my_list), 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]

print(my_list)
