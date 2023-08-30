# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import
# randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

randint_num = randint(0, 2)
result = 0
count = 10
while count > 0:
    u_num = int(input("Введите своё число"))
    if randint_num == u_num:
        result = "You Win"
        break
    elif randint_num > u_num :
        count -= 1
        print(f'Вы потерпели неудачу у вас осталось попыток {count}, заданное число компьютером больше')
    elif randint_num < u_num:
        count -= 1
        print(f'Вы потерпели неудачу у вас осталось попыток {count}, заданное число компьютером меньше')
else:
    print('Исчерпаны все попытки. Сожалею')
    quit()

print(result)
