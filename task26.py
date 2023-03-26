# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def exponentiation(a, b):
    if b == 0:
        return 1
    return exponentiation(a, b-1) *a

a= int(input("Введите число: "))
b= int(input("Введите степень числа: "))
print(f"Число {a} в степени {b} = {exponentiation(a, b)}")
