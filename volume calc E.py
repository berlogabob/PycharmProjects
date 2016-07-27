# -*- coding: utf-8 -*-
def dialog():
    answer = input("Скрипт переводит число, записанное компьютерным способом экспоненциальной записи в нормализованную \n в качестве разделителя дробной части используйте ТОЧКУ ""\n""хотите ввести число? (да/нет)    ")
    if answer == "да" or answer == "Да" or answer == "д" or answer == "ДА" or answer == "Д" or answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES":
        userinp()
    elif answer == "нет" or answer == "Нет" or answer == "Н" or answer == "н" or answer == "НЕТ" or answer == "N" or answer == "No" or answer == "n" or answer == "no" or answer == "NO":
        print("\n завершено")
    else:
        print("\n \n введено некорректное значение")
def userinp():
    mantissa = float(input("Введите мантиссу числа    "))
    exponenta = float(input("какова эксонента числа?    "))
    print(mantissa * 10 ** exponenta)
    dialog()
dialog()