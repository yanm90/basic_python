import json

with open('text_7.txt', 'r', encoding='utf-8') as file:
    len_file = len(file.readlines())
    file.seek(0)
    firms = {}
    average_profit = [0, 0]
    for i in range(len_file):
        content = file.readline().split()
        profit = int(content[2]) - int(content[3])
        firms.update({content[0]: profit})
        if profit > 0:
            average_profit[0] += profit
            average_profit[1] += 1
average_profit = {'average_profit': round(average_profit[0] / average_profit[1], 2)}
result_list = [firms, average_profit]

with open('7.json', 'w', encoding='utf-8') as wr_json:
    json.dump(result_list, wr_json, ensure_ascii=False, indent=4)
