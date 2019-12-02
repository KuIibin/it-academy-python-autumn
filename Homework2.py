
# Задание 1: программа считает сумму заказа

rubles = int(input("Введите колличество рублей: "))
cents = int(input('введите колличество копеек: '))
c_purchases = int(input('Количество покупок '))
r_cents = cents / 100
price = rubles + r_cents
total_price = price * c_purchases
total_price_c = round(total_price // 1)
total_price_p = round((total_price % 1) * 100)
print('Спасибо, что сделали покупку у нас.')
print('Общая цена ', total_price_c, ' рублей ', total_price_p, ' копеек.')

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
