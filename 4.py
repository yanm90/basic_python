origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

answer_list = [i for i in origin_list if origin_list.count(i) == 1]

print(answer_list)
