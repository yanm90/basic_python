from itertools import count
from itertools import cycle

# Проверка на ввод чисел и ввод двух значений
while True:
    try:
        numbers = input('Начало и конец списка через пробел: ')
        numbers = numbers.split()
        for num, i in enumerate(numbers):
            numbers[num] = int(i)
        if len(numbers) == 2:
            break
        else:
            print('Нужно ввести два числа')
    except ValueError:
        print('Ошибка ввода данных')

result_list = []
for i in count(numbers[0]):
    if i > numbers[1]:
        break
    else:
        result_list.append(str(i))
print(f'Результат: {", ".join(result_list)}')

# Проверка на ввод числа
while True:
    try:
        repeat = int(input('Cколько раз повторить список?\n'))
        break
    except ValueError:
        print('Ошибка ввода данных')

c = 0
repeat_list = []
for i in cycle(result_list):
    if c == repeat * len(result_list):
        break
    else:
        repeat_list.append(str(i))
        c += 1

print(f'Результат: {", ".join(repeat_list)}')
