def int_func(word):
    """
    Проверяет переменную на тип данных str, нижний регистр и латиницу
    При успешноц проверке возвращает с заглавной буквы
    При ошибке возвращает 'error'

    int_func('word') -> 'Word'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if type(word) != str:
        return 'error'
    else:
        for i in word:
            if i in alphabet:
                continue
            else:
                return 'error'
        return word.title()


my_str = input('Строка из строчных латинских слов:\n')
answer = []

for i in my_str.split():
    answer.append(int_func(i))

print(' '.join(answer))
