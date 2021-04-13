'''
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение»
из этого пути имени файла (без расширения).
'''

import os
from pathlib import Path


def get_file_name(file_name):

    if Path(file_name).exists():
        a = Path(file_name).resolve()
        print(a)
        print(a.stem)
    else:
        print('Нет такого файла')


if __name__ == '__main__':

    file = 'lesson_3_test.txt'
    get_file_name(file)



