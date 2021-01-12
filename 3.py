def input_number():
    """Пользовательский ввод числа с проверкой на type(int)"""
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except ValueError:
            print('Ошибка. Введено не число')

# Создание списка из трех строк n + nn + nnn
n = str(input_number())
n_list = [n]
for i in range(2):
    n_list.append(n_list[i] + n)

# Перевод созданного списка из str в int
for i in range(len(n_list)):
    n_list[i] = int(n_list[i])

# подсчет n + nn + nnn
answer = 0
for i in range(len(n_list)):
    answer = answer + n_list[i]

print(f'{n_list[0]} + {n_list[1]} + {n_list[2]} = {answer}')