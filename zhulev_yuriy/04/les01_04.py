# coding: utf-8

# Python. Быстрый старт.
# Занятие 4.

# Домашнее задание: 
#                  создать новое действие - дублировать файл, который укажет пользователь;
#                  создать действие - удаление файлов с окончанием '.dupl' в указанной директории.

import os
import sys
import shutil
import psutil


print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = ''
while answer != 'q':
    answer = input("Давайте поработаем? (Y/N/q)")
        
    if answer == 'Y' or 'y':
        print("Отлично, хозяин!")
        print("Я умею:")
        print(" [1] - выведу список файлов")
        print(" [2] - выведу информацию о системе")
        print(" [3] - выведу список процессов")
        print(" [4] - продублирую файлы в текущей директории")
        print(" [5] - создать дубликать конкретного файла")
        print(" [6] - удаление файлов .dupl")
        
        do = int(input("Укажите номер действия: "))
        
        if do == 1:
            print(os.listdir())
            
        elif do == 2:
            print("Вот что я знаю о системе")
            print("Количество процессоров: ", psutil.cpu_count())
            print("Платформа: ", sys.platform)
            print("Кодировка файловой системы: ", sys.getfilesystemencoding())
            print("Текущая директория: ", os.getcwd())
            print("Текущая пользователь: ", os.getlogin())
            
        elif do == 3:
            print(psutil.pids())
            
        elif do == 4:
            print("==Дублирование файлов==")
            file_list = os.listdir()
            i = 0
            # Цикл while будет выполняться пока i будет меньше длины списка file_list
            while i < len(file_list):
                # Необходимо выполнить проверку isfile, т.к. при попытке копирования директории будет возникать ошибка
                if os.path.isfile(file_list[i]):
                    shutil.copy(file_list[i], file_list[i] + '.dupl')
                # Чтобы цикл имел возможность завершиться нужно изменять переменную цикла        
                i += 1
        elif do == 5:
            print("==Дублирование файла==")
            file_name = str(input("Введите имя файла: "))
            if os.path.isfile(file_name):
                shutil.copy(file_name, file_name + '.dupl')
                print('Создан дубликат файла ' + file_name)
            else:
                print('Файл не найден.')
        elif do == 6:
            print("==Удаление файлов .dupl==")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    print(file_list[i])
                f = file_list[i]
                if f.endswith('.dupl'):
                    os.remove(file_list[i])
                i += 1
        else:
            print('Неверный номер действия!!!')
       
    elif answer == 'N' or 'n':    
        print("До свидания!")
    else:
        print("Неизвестный ответ")    