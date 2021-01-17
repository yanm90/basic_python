print('Внесите товары в базу данных\nДвойной Enter - завершение ввода данных\n')

base = []
products = []

while True:
    product = input('Введите через пробел и нажмите Enter\n[Название] [Цена] [Количество] [Еденица измерения]\n')

    if product == '':
        break

    product = product.split()
    products.append(product)
    product = {'Название': product[0], 'Цена': product[1], 'Количество': product[2], 'Еденица измерения': product[3]}
    base.append(product)

for n, i in enumerate(base, 1):
    i = (n, i)
    base.pop(n-1)
    base.insert(n-1, i)

print('Готовая структура:\n', base, '\n\nАналитика:')

keys = list(base[1][1].keys())
values = []

for i in range(len(keys)):
    analytic = []
    for ii in products:
        analytic.append(ii[i])
    values.append(analytic)

analytics = dict(zip(keys, values))
print(analytics)