# Задача 26:  Напишите программу, которая на вход принимает два числа 
# A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def stepen(a,b):
#     if a == 0:
#         return 0
#     elif b == 0:
#         return 1
#     return a*stepen(a,(b-1))

# a = int (input('Введите число а: '))
# b = int (input('Введите число b: '))
# print (stepen(a,b))
        

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую 
# сумму двух целых неотрицательных чисел. Из всех арифметических 
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

# def summa(a,b):
#     if ((a==0) & (b==0)):
#         return 0
#     elif ((a==0) or (b==0)):
#             if b>a:
#                 return summa(a,(b-1))+1
#             elif b<a:
#                 return summa((a-1),b)+1
#     return summa((a-1),(b-1))+1+1

# a = int (input('Введите число а: '))
# b = int (input('Введите число b: '))
# print (summa(a,b))  