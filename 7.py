from itertools import count


def fact(el):
    c = 1
    for i in count(1):
        if i > el:
            break
        else:
            c = c * i
            yield c


for num, i in enumerate(fact(19), 1):
    print(f'Факториал {num} равен {i}')
