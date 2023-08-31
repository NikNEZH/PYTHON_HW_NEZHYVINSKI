# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

number_a = int(input("Введите числитель 'a': "))
number_b = int(input("Введите знаменатель 'b': "))
number_c = int(input("Введите числитель 'c': "))
number_d = int(input("Введите знаменатель 'd': "))

sum_numerator = number_a * number_d + number_c * number_b
sum_denominator = number_b * number_d

product_numerator = number_a * number_c
product_denominator = number_b * number_d

print(f"Сумма дробей: {sum_numerator}/{sum_denominator}, Произведение дробей:{product_numerator}/{product_denominator}")


fraction1 = fractions.Fraction(number_a, number_b)
fraction2 = fractions.Fraction(number_c, number_d)
print(fraction1 + fraction2)
print(fraction1 * fraction2)
