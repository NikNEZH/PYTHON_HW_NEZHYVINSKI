# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = num_2 = int(input("Enter number: "))
base = 16
result: str = ''
hex_digits: str = "0123456789abcdef"
while num:
    rem = num % base
    num //= base
    result = hex_digits[rem] + result

print(f'Число {num_2} в {base}-ичной системе счисления будет: {result}')
print(hex(num_2))
