# Задача. Дан текст (строк может быть много,
# разделенных \n). Выведите слово, которое в
# этом тексте встречается чаще всего. Если
# таких слов несколько, выведите то, которое
# меньше в лексикографическом порядке.

# sent = input('Введите предложение: ')
# print('Введенная строка: ', sent)
# dct = {}
# sent_lst = sent.split()
# print('После сплита получилось: ', sent_lst)
# for el in sent_lst:
#     dct[el] = dct.get(el, 0) + 1
# print('Словарь посде get: ', dct)
# print('Список после get: ', sent_lst)
# lst = sorted(dct.items(), key=lambda item: (-item[1], item[0]))
# print('Словарь после сортировки: ', lst)
# print('Ответ по заданию: ', lst[0][0])

# second solution

string = input("enter space separated numbers: ")

num_list = string.split()
result_dict = {}

for num in num_list:
    result_dict[num] = result_dict.get(num, 0) + 1

def maxkey(result_dict):
    values = list(result_dict.values())
    keys = list(result_dict.keys())
    return keys[values.index(max(values))]


print(maxkey(result_dict))
