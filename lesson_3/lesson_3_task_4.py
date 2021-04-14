'''
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать
открытие файла и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.
'''

import os
import random


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
            # print(f.readlines())
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