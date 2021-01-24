from functools import reduce

my_f = lambda prev_el, el: prev_el * el

print(reduce(my_f, [i for i in range(100, 1000 + 1, 2)]))
