def input_number(comment):
    """Пользовательский ввод числа с проверкой на type(int)"""
    while True:
        try:
            number = int(input(comment + ': '))
            return number
        except ValueError:
            print('Ошибка. Нужно ввести число')


profit = input_number('Выручка фирмы')
expense = input_number('Расходы фирмы')
result = profit - expense

if result > 0:
    print('Поздравляю! Вы работаете с прибылью')
    rent = result / profit
    # print('Рентабельность фирмы: ' + str('%.2f' % rent) + '%')
    print(f'Рентабельность фирмы: {rent:.2f}%')
    staff = input_number('Количество сотрудников')
    staff_profit = result / staff
    # print('Рентабельность на сотрудника: ' + str('%.2f' % staff_profit) + ' руб')
    print(f'Рентабельность на сотрудника: {staff_profit:.2f} руб')
else:
    print('Вы работаете в убыток :(')
