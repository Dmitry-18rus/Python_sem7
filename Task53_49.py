# file_path = ' data.txt'
# with open(file_path, 'w') as f:
#     f.write('Hello world')

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

file_path = 'tel_sprav.txt'
def vvod():
    vizov = int (input('Введите команду: \n1 - Вывод всех данных \n2 - Добавление контакта \n3 - Поиск контакта\n:'))
    return vizov

def vivod_dannih(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f:
            mass = line.strip().split(',')
            for i in range(len(mass)):
                print(mass[i], end=" ")
            print("")
        f.read()
    return True

def add_contact(file_path):
    with open(file_path, 'a', encoding='UTF-8') as f:
        surname = input('Введите данные контакта: Фамилия: ')
        name = input('Имя: ')
        patronymic = input('Отчество: ') 
        phone = input('Номер телефона: ')
        print(f'Контакт успешно добавлен --> {surname} {name} {patronymic} {phone}')
        f.write ('\n' + f'{surname} {name} {patronymic} {phone}')
    return True
    
           
def search_cont(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        poisk = input('Введите имя или фамилию контакта: ')
        for line in f:
            if poisk in line:
                mass = line.strip().split(',')
                for i in range(len(mass)):
                    print(mass[i], end=" ")
                print("")
        f.read()    
    return True

input_ = vvod()

if input_ ==1:
    vivod_dannih(file_path)
elif input_ ==2:
    add_contact(file_path)
elif input_ ==3:
    search_cont(file_path)
else:
    print("Выбран недопустимый параметр! Попробуйте снова! ")
        