# Пользовательский ввод строки
user_word = input('Введите слово: ')
print('Значение переменной: ' + user_word + '\nТип переменной: ' + type(user_word).__name__ + '\n')

# Пользовательский ввод числа с проверкой на type(int)
while True:
    try:
        user_number = int(input('Введите число: '))
        break
    except ValueError:
        print('Ошибка. Нужно ввести число')
        pass
print('Прверка пройдена. Введено число:', user_number)