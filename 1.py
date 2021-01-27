with open('1_file.txt', 'w', encoding='utf-8') as file:
    while True:
        my_str = input()
        if my_str == '':
            break
        else:
            file.write(my_str + '\n')
