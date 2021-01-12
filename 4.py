def input_number():
    """Пользовательский ввод числа с проверкой на type(int) и положительное значение"""
    while True:
        try:
            number = int(input('Введите число: '))
            if number > 0:
                return number
            else:
                print('Число должно быть положительным')
        except ValueError:
            print('Ошибка. Введено не число')

user_number = input_number()

# Получаем последнюю цифру числа при помощи остатка от деления на 10
max = user_number % 10

# Отсекаем последнюю цифру от введенного числа при помощи деления на 10 без остатка
user_number = user_number // 10

# С помощью цикла while сравнимаем и отсекаем последние цифры, пока не кончится введенное число
while user_number > 0:
    # Если последняя оставшаяся цифра больше отсеченной - она становится максимальной
    if user_number % 10 > max:
        max = user_number % 10
    # Снова отсекаем последнюю цифру
    user_number = user_number // 10

print('Самая большая цифра: ', max)