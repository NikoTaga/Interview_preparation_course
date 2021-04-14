'''
2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
'''


def run():

    input_num = input('Введите число ')

    if input_num.isdigit():
        print(f'{input_num} - целое число')
    else:
        try:
            is_float = float(input_num)
        except ValueError:
            print('Ввели неправильные данные')

        else:
            print(f'{is_float} - дробное число')
            print(comp_num(is_float))


def comp_num(num):

    int_part = int(num // 1)
    fract_part = int(str(num)[len(str(int_part)) + 1:])
    return int_part == fract_part


if __name__ == '__main__':
    run()







