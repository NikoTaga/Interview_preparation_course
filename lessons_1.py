
def multiplication_table(a, b):
    """Функция вывода таблицы умножения AxB"""
    for i in range(a):
        for j in range(b):
            print(f'{i + 1} x {j + 1} = {(i + 1) * (j + 1)}')
        print()



if __name__ == '__main__':
    a = 6
    b = 2
    multiplication_table(a, b)