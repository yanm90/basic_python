import random

original_list = [random.randint(0, 1000) for i in list(range(0, random.randint(2, 20)))]
answer_list = [i for num, i in enumerate(original_list[1:]) if i > original_list[num]]

print(original_list)
print(answer_list)
