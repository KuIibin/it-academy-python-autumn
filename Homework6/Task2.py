# Создайте декоратор, который хранит в файле
# результаты вызовы функций (за все время,
# не только текущий запуск программы)

def dec(sqrt):
    def wrapper(x):
        result = sqrt(x)
        f = open('Homework6/t2-results.txt', 'a')
        f.write('Func "sqrt" has result: {}\n'.format(result))
        f.close()
    return wrapper


@dec
def sqrt(x):
    return int(x ** 0.5)

sqrt(100)
sqrt(400)
sqrt(900)
