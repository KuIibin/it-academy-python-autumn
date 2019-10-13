# from random import random

# def dec(fun):
#     all_sum = 0
#     def wrapper():
#         nonlocal all_sum
#         all_sum += fun()
#         return all_sum
#     return wrapper

# @dec
# def func():
#     return random()

# print(func())
# print(func())
# print(func())
# print(func())

def dec(fun):
    all_sum = 0
    def wrapper():
        nonlocal all_sum
        all_sum += 1
        return fun()
    return wrapper

@dec
def func():
    return "a;fjja;"

print(func())