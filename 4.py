my_str = input('Введите строку: ')

my_str = my_str.split()

for n, i in enumerate(my_str, 1):
    print(n, i[:10])