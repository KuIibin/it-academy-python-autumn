# Оформите решение задач из прошлых домашних работ в
# функции. Напишите функцию runner.
#   runner() – все фукнции вызываются по очереди
#   runner(‘gen_numbers’) – вызывается только функцию gen_numbers. 
#   runner(‘func’, ‘func1’...) - вызывает все переданные функции 

import AllTasksInFunc

all_func = [el for el in dir(AllTasksInFunc) if not el.startswith('__')]

def runner(*func_name):
    if len(func_name) == 0:
        func_name = all_func
    for name in func_name:
        func = getattr(AllTasksInFunc, name)
        func()

runner('is_palindrom')
