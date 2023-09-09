# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def no_hesh_function(**kwargs):
    my_dict = dict()
    for key, value in kwargs.items():
        if not isinstance(key, (int, float, str)):
            key = str(key)
        my_dict[value] = key

    return my_dict


result = no_hesh_function(test=453, no_problem=678, hello=123)
print(result)

