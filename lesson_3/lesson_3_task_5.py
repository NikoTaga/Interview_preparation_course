'''
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть
строковых значений заменить на значения типа example345 (строка+число).
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
'''

import os
import random
import re


def func_1():

    list_int = [random.randint(MIN_ITEM_INT, MAX_ITEM_INT) for _ in range(SIZE)]
    list_str = [''.join(chr(random.randint(MIN_ITEM_STR, MAX_ITEM_STR)) for _ in range(SIZE_ELEM)) for _ in range(SIZE)]

    try:
        with open(FILE, 'x') as f:
            pass
    except FileExistsError:
        print(f'Файл с именем {FILE} уже существует')

    try:
        with open(FILE, 'w', encoding='UTF-8') as file:
            for i, j in list(zip(list_int, list_str)):
                file.write(f' {i}  {j} \n')
        func_2(os.path.join(FILE))
    except FileNotFoundError:
        print('файл не найден')


def func_2(file):

    try:
        with open(file, 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                print(i[:-1])
    except FileNotFoundError:
        print('файл не найден')


if __name__ == '__main__':

    FILE = 'lesson_3_test3.txt'

    SIZE = 10
    SIZE_ELEM = 7

    MIN_ITEM_INT = 0
    MAX_ITEM_INT = 100

    MIN_ITEM_STR = 97  # 1040
    MAX_ITEM_STR = 122  # 1103

    func_1()