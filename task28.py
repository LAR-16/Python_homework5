# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# def sum(a, b):
#     if a==0 :
#         return b
#     return sum(a-1, b) +1 
    
# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# print(sum(first, second))


# 2-ой вариант решения
def sum(a, b):
    a+=1
    b-=1
    if b==0 :
        return a
    return sum(a, b) 
    
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
print(sum(first, second))
