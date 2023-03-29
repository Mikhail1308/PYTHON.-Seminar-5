# Задача 26: 
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def power(base, exp):
#     if (exp == 1):
#         return (base)
#     if (exp != 1):
#         return (base * power(base, exp - 1))
# base = int(input("Введите число: "))
# exp = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", power(base, exp))


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x, -n)
    if n%2 == 0:
        return power(x,n//2)*power(x,n//2)
    else:
        return power(x, n - 1)*x

x = int(input('Введите число: '))
n = int(input('Введите степень числа: '))
print(f'Результат возведения в степень равен: {power(x,n)}')
