# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def func():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


my_iter = iter(func())
while True:
    print(next(my_iter), '\t')


