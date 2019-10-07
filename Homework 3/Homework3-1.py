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
