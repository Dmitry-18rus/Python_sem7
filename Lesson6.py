# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def arr_input(a,n,d):
#     arr = [a]
    
#     for i in range(2,n+2):
#         arr.append(a+(i-1)*d)
#     return arr

# a = int (input("введите первый элемент a1: "))
# n = int (input("введите кол-во элементов n: "))
# d = int (input("введите число d: "))
# print (arr_input(a,n,d))

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного максимума)

# import random
# def create_list(i):
#     list_= []
#     for j in range(i):
#         list_.append(random.randint(1,9))
#     return list_

# i = int (input("введите длину массива: "))
# min_ = int (input("введите минимум диапазона: "))
# max_ = int (input("введите максимум диапазона: "))
# arr = create_list(i)
# res_arr = []
# for item in range(i):
#     if min_ < arr[item] < max_:
#         res_arr.append(item)
# print(arr)
# print (res_arr)