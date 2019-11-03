def total_price():
    '''программа считает сумму заказа'''
    m = int(input("Введите колличество рублей: "))
    n = int(input('введите колличество копеек: '))
    k = int(input('Количество покупок '))
    n = n / 100
    l = m + n
    price = l * k
    price_c = round(price // 1)
    price_p = round((price % 1) * 100)
    print('Спасибо, что сделали покупку у нас.')
    print('Общая цена ', price_c, ' рублей ', price_p, ' копеек.')

def el_less_5():
    '''Выводит все элементы, которые меньше 5'''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for element in a:
        if element < 5:
            print(element)


def num_divided():
    '''Определить, делится ли число на 17'''
    a = int(input('Введите число '))
    b = a % 17

    if b == 0:
        print('Поздравляю! Это число делится на 17')
    else:
        print('Очень жаль. Я надеюсь, в следующий раз тебе повезет')

def both_lst():
    '''список из двух списков'''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    stack = []
    for el in a:
        if el in b:
            stack.append(el)
    print(stack)

both_lst()
"""
# дополнительное задание
# Определите, является ли число палиндромом (читается слева
# направо и справа налево одинаково).
# Число положительное целое, произвольной длинны

# подсмотрел решение. зато разобрался)
num = int(input('Enter number:'))
test = num
dopel = 0
while 1:
    dopel += num % 10
    print(dopel)
    num //= 10
    print(num)
    if not num:
        break
    dopel *= 10
    print(dopel)
    print('end iteration')
if test == dopel:
    print('palindrome')
else:
    print('not palindrome')


# Числа фибоначи
# первые два числа равны либо 1 и 1, либо 0 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел

n = int(input('Введите колличество чисел: '))
x = [1, 1]
for element in range(2, n):
    x.append(x[-1] + x[-2])
print(x)

# Задание: Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.

x = input('Введите строку: ')
x = x.split()
for i in range(0, len(x)):
    x[i] = x[i].strip(',.!?')
idFirst = 0
for y in range(1, len(x)):
    if len(x[idFirst]) < len(x[y]):
        idFirst = y

print('Самое длинное слово - это "' + x[idFirst] + '"')

# Вводится строка. Требуется удалить из нее повторяющиеся
# символы и все пробелы. Например, если было введено
# "abc cde def", то должно быть выведено "abcdef"

# вводим строку и удаляем из нее все пробелы путем замены
x = input('Введите предложение: ')
x = x.replace(' ', '')
# создаем новую строку и пишем цикл for
y = ''
for i in x:
    if i not in y:
        y = y + i
print(y)

 
# Посчитать количество строчных (маленьких) и прописных (больших)
# букв в введенной строке. Учитывать только английские буквы.

sents = input('Введите предложение: ')
sents = sents.replace(' ', '')
upperCount = 0
lowerCount = 0

for i in sents:
    if 'a' <= i <= 'z':
        lowerCount += 1
    elif 'A' <= i <= 'Z':
        upperCount += 1

print('Маленьких - {lowerCount} букв'.format(lowerCount=lowerCount))
print('Больших - {upperCount} букв'.format(upperCount=upperCount))

# Write a program that prints the numbers from 1 to 100,
# but for multiples of three print “Fizz” instead of the number
# and for multiples of five print “Buzz”. For numbers which are
# multiples of both three and five, print “FizzBuzz”.

lst = []
for el in range(1, 101):
    if (el % 15) == 0:
        el = 'FizzBuzz'
        lst.append(el)
    elif (el % 3) == 0:
        el = 'Fizz'
        lst.append(el)
    elif (el % 5) == 0:
        el = 'Buzz'
        lst.append(el)
    else:
        lst.append(el)
print(lst)

# List practice

# Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb',
# 'bc', 'bd'].
lst1 = [str(q + w) for q in 'ab' for w in 'bcd']
print(lst1)
# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
lst2 = lst1[::2]
print(lst2)
# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst3 = [x + y for x in '1234' for y in 'a']
print(lst3)
# Simultaneously remove the element '2a' from the above list and print it.
print(lst3.pop(1))
# Copy the above list and add '2a' back into the list such that the
# original is still missing it.
lst3_copy = lst3[:]
lst3_copy.insert(1, '2a')
print(lst3_copy)

# Tuple practice


# Create the list ['a', 'b', 'c'], then create a tuple from that list.
lst1 = [el for el in 'abc']
print(lst1)
tpl1 = tuple(lst1)
print('subtask1 done. answer is ', tpl1)

# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
# (Hint: the material needed to do this has been covered, but
# it's not entirely obvious)

x1 = 'a'
x2 = 'b'
x3 = 'c'
# создаем кортеж с помощью конкатенации
tpl2 = tuple(x1 + x2 + x3)
# с помощью итерирования копируем все элементы из кортежа в список
lst2 = []
for el in tpl2:
    lst2.append(el)
# не помню уже почему, но сразу я пробовал решение ниже,
# а оно не сработало.
lst3 = list(tpl2)
print(tpl2)
print('subtask2 done. answer is ', lst3)

# Make the following instantiations simultaneously: a = 'a', b=2,
# c='gamma'. (That is, in one line of code).
a, b, c = 'a', 2, 'gamma'
print('subtask3 done. answer is ', a, b, c)


# Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'. Verify that the length is actually
# 1 by using the len() function.
x = ('a', 'b', 'c')
y = (x, )
print('Длина запрашиваемого списка - ', len(y))
print(y)

# Define a dict comprehension which returns a dictionary
# where the keys are numbers between 1 and n (both included)
# and the values are square of keys. n – function argument.
# Default is 20.
# Define a code which count and return the numbers of each
# character in a count_me_string argument.
# Example:
# If the following string is given as argument to the function:
# abcdefgabc
# Then, the return result of the function should be:
# {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}

number = int(input('Введите число: '))
dct = {el: el**2 for el in range(1, number + 1)}
print(dct)

sent = input('Введите предожение: ')
dct2 = {el: sent.count(el) for el in sent}
print(dct2)

# second solution
sent2 = input('Введите предожение: ')
dctWithFrequency = {}

for el in sent2:
    if el in dctWithFrequency:
        dctWithFrequency[el] += 1
    else:
        dctWithFrequency[el] = 1
print(dctWithFrequency)

# Задача. Дан текст (строк может быть много,
# разделенных \n). Выведите слово, которое в
# этом тексте встречается чаще всего. Если
# таких слов несколько, выведите то, которое
# меньше в лексикографическом порядке.


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

# Дан список стран и городов каждой страны.
# Затем даны названия городов. Для каждого города
# укажите, в какой стране он находится.

number_contries = int(input('Введите колличество стран: '))

countries_and_cityes = {}
for el in range(number_contries):
    country, *city = input('Введите Страну и ее город: ').split()
    for elem in city:
        countries_and_cityes[elem] = country
print('Словарь из Стран и их городов: ', countries_and_cityes)

number_cityes = int(input('Введите к-во городов для проверки: '))
cityes = []
print('Вводите название городов, которые хотите проверить: ')

for el in range(number_cityes):
    cityes.append(input())
for el in cityes:
    print(el, 'находится в', countries_and_cityes.get(el))
    
# Даны два списка чисел. Посчитайте, сколько
# чисел содержится одновременно как в первом
# списке, так и во втором.

string1 = set(input('Введите 1-ый список чисел: ').split())
string2 = set(input('Введите 2-ый список чисел: ').split())
print('Числа в обоих множествах', len(string1 & string2))

# Даны два списка чисел. Посчитайте, сколько
# чисел входит только в один из этих списков

string1 = set(input('Введите 1-ый список чисел: ').split())
string2 = set(input('Введите 2-ый список чисел: ').split())
print('', len(string1 ^ string2))"""