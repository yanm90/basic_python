with open('text_3.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    for num, _ in enumerate(content):
        content[num] = content[num].split()
        content[num][1] = float(content[num][1])

losers = []
for i in content:
    if i[1] < 20000:
        losers.append(i[0])
print(f'Оклад менее 20000: {", ".join(losers)}')

middle = round(sum([i[1] for i in content]) / len(content), 2)
print(f'Средняя зп: {middle}')
