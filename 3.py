def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


print(my_func(7, 3, 10))
