def input_number():
    """Пользовательский ввод числа с проверкой на type(int)"""
    while True:
        try:
            seconds = int(input('Введите количество секунд: '))
            return seconds
        except ValueError:
            print('Ошибка. Введено не число')

def hour_min_sec(seconds):
    """Перевод секунд в часы, минуты и секунды с помощью деления без остатка и остатка от деления"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return (hours, minutes, seconds)

change = (hour_min_sec(input_number()))

print(f'Часов: {change[0]}\nМинут: {change[1]}\nСекунд: {change[2]}')