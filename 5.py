my_list = [7, 5, 3, 3, 2]

new_element = int(input("Введите новый элемент: "))

my_list.reverse()

for i in my_list:
    if new_element <= i:
        my_list.insert(my_list.index(i), new_element)
        break
    else:
        my_list.append(new_element)
        break

my_list.reverse()

print(my_list)
