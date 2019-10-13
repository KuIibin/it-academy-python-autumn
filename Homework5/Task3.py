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
