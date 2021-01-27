with open('text_6.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

school = {}

for i in content:
    i = i.split()
    dict_key = i.pop(0)
    dict_val = 0
    for ii in i:
        hours = ''
        for iii in ii:
            try:
                iii = int(iii)
                hours += str(iii)
            except ValueError:
                continue
        try:
            dict_val += int(hours)
        except ValueError:
            continue
        school.update({dict_key[:-1]: dict_val})

print(school)
