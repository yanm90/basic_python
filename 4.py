my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
origin_file = open('text_4.txt', 'r', encoding='utf-8')
my_file = open('4_practice_file.txt', 'w', encoding='utf-8')

len_original_file = len(origin_file.readlines())
origin_file.seek(0)

for i in range(len_original_file):
    content = origin_file.readline().split()
    if content[0] in my_dict:
        content[0] = my_dict.get(content[0])
        my_file.write(" ".join(content) + '\n')

origin_file.close()
my_file.close()
