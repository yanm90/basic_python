def my_func(x, y):
    if (type(x) == int or float) and (type(y) == int and y < 0):
        result = x
        for i in range(1, abs(y)):
            result = x * result
        return 1 / result
    else:
        return 'Ошибка в вводе данных'


print(my_func(5, -5))
