#def sum_(a,b):
#    return a+b
#sum(1, 2.5)
'''
def very_big_func(a, b=0, *args, c, d=1, **kwargs):

    print(a, b, args, c, d, kwargs)

very_big_func(1, 2, 3, c=5, e=7)
very_big_func(1, 2, 3, c=5, e=7)
very_big_func(1, 2, 3, c=1)

# def one_more(a, *, c):

# one_more(1, 2):
# one_more(3, c=0)

def print_func(a, b, *, c, d):
    print(a, b, c, d)

pos_arg = [1, 2]
pos_tuple = (1, 2, 3, 4)
named_dict = {'c': 5, 'd': 7}

    print_func(*pos_arg, **named_dict)
    print_func(*pos_tuple, **named_dict)

def fun_func(a):
    print(a)

fun_func([1, 2, 3])
fun_func({1: 2, 3: 4})
fun_func(1)
fun_func('stri"ng')

def strange_func():
    print('strange')

fun_func(strange_func)
fun_func(strange_func())
'''

def func(num):
    sum = 0
    while num:
        digit = num % 10
        sum += digit
        num //= 10
    return(sum)
print(func(1234))
