my_list = [110, 'homework', ('word1', 'word2'), None, {'key1': 123, 'key2': False}, True, [], 1.75]

for number, i in enumerate(my_list):
    print(number, type(i).__name__)
