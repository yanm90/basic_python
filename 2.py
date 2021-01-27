with open('text_1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print('Всего сторок:', len(lines))
    for num, i in enumerate(lines, 1):
        print(f'Строка {num}: {len(i.split())} слов')
