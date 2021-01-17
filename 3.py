month = int(input('Введите номер месяца: '))

# Решение через dict

year = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for i in year.items():
    if month in i[1]:
        print(i[0])

# Решение через list

year = [i for i in range(1, 13)]

for i in year:
    if month == i:
        if year.index(i) < 2 or year.index(i) == 11:
            print('зима')
        elif year.index(i) >= 2 and year.index(i) < 5:
            print('весна')
        elif year.index(i) >= 5 and year.index(i) < 8:
            print('лето')
        elif year.index(i) >= 8 and year.index(i) < 11:
            print('осень')
    elif month > len(year):
        print('Неправильный номер месяца')
        break
