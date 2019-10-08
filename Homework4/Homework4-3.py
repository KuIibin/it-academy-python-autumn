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
