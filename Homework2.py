
# Задание 1: программа считает сумму заказа

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

# Задача 1
# Выведите все элементы, которые меньше 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in a:
    if element < 5:
        print(element)


# Определить, делится ли число на 17
a = int(input('Введите число '))
b = a % 17

if b == 0:
    print('Поздравляю! Это число делится на 17')
else:
    print('Очень жаль. Я надеюсь, в следующий раз тебе повезет')


# Даны списки:
# Нужно вернуть список, который состоит из элементов
# общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

stack = []
for el in a:
    if el in b:
        stack.append(el)
print(stack)

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
    print(dopel) # for check
    num //= 10
    print(num) # for check
    if not num:
        break
    dopel *= 10
    print(dopel) # for check
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
# подсказку для решения нашел на стек оверфлоу
'''