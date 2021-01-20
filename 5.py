def sum_my_digits(ex_com=0):
    global result
    while ex_com == 0:
        local_result = 0
        sum_list = input('Введите через пробел числа для суммирования: ')
        sum_list = sum_list.split()

        for i in sum_list:
            if i.isdigit():
                i = int(i)
                local_result = local_result + i
            elif i == 'q':
                ex_com = 1
            else:
                print('Нужно вводить только числа!\nДля заверщения нажмите Q')

        result = result + local_result
        print(f'{local_result} ({result})')


result = 0

sum_my_digits()
