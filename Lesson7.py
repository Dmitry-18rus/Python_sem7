# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм 
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# vvod = "пара-ра-рам рам-пам-папам па-ра-па-да"
# glas = "у е ё а о э я и ы ю"
# res = []
# sum_ = 0
# stih = vvod.split()
# # print(stih)
# for fraz in stih:
#     count = 0
#     slov = fraz.split("-")
#     # print(slov, end="")
#     for j in glas:
#         for i in range(len(slov)):
#             for k in range(len(slov[i])):  
#                 if slov[i][k] == j:
#                     count +=1
#     res.append(count)
#     # print(res)
# for i in range(len(res)):
#     sum_ += res[i]
# if ((sum_/len(res)) == res[0]): 
#     print ("Парам пам-пам")
# else:
#     print("Пам парам")
    
        

  
# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки 
# и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, 
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой 
# ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
#   1   2   3   4   5   6
#   2   4   6   8   10  12
#   3   6   9   12  15  18
#   4   8   12  16  20  24
#   5   10  15  20  25  30
#   6   12  18  24  30  36

def print_operation_table(operation, num_rows=6, num_columns=6):
    num_rows=6
    x=num_rows
    num_columns=6
    y=num_columns
    for i in range(1,x+1):
        for j in range(1,y+1):
            print(operation(i,j),end=' ')
        print()
print_operation_table(lambda x, y: x*y)


# вариант 1
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     table_list = []
#     for i in range(1, num_rows + 1):
#         line_list = []
#         for j in range(1, num_columns + 1):
#             el = operation(i, j)
#             line_list.append(el)
#         table_list.append(line_list)
#     for line in table_list:
#         print(*line)
# print_operation_table(lambda x, y: x*y)

# вариант 2
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             el = operation(i, j)
#             print(el, end=' ')
#         print()
# print_operation_table(lambda x, y: x*y)

# вариант 3
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     table_list = [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1)]
#     for line in table_list:
#         print(*line)


# print_operation_table(lambda x, y: x*y)