def input_number(comment):
    """Пользовательский ввод числа с проверкой на type(int)"""
    while True:
        try:
            number = int(input(comment + ': '))
            return number
        except ValueError:
            print('Ошибка. Нужно ввести число')


a = input_number('Результат в первый день')
b = input_number('Искомый результат')
c = 1

while a < b:
    a = a * 1.1
    c += 1
    # print(str(c) + ' день: ' + '%.2f' %a + ' км')
    print(f'{str(c)} день: {a:.2f} км')

print('\nРезультат:', c)
