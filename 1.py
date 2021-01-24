from sys import argv

try:
    user_data = [int(i) for i in argv[1:]]
    salary = (user_data[0] * user_data[1]) + user_data[2]
    print(f'Заработная плата: {salary} руб')
except:
    print('Ошибка ввода данных.\nВведите 3 чила: количесвто часов, оплата за час, премия')
