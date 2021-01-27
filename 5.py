with open('5_practice_file.txt', 'w+', encoding='utf-8') as file:
    file.write(input('Числа разделенные пробелами: '))
    file.seek(0)
    content = file.read().split()

sumlist = []

for i in content:
    try:
        i = int(i)
        sumlist.append(i)
    except ValueError:
        continue

print(sum(sumlist))
