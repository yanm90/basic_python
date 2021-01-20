def division(arg_1, arg_2):
    """Первый аргумент делим на второй"""
    while True:
        try:
            return round(arg_1 / arg_2, 2)
        except ZeroDivisionError:
            return 'Ошибка. Деление на 0'


print(division(27, 7))
