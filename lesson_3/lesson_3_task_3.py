'''
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
'''


def get_dict(keys, values):

    result_dict = {}
    for i, key in enumerate(keys):
        try:
            result_dict[key] = values[i]
        except IndexError:
            result_dict[key] = None
    print(result_dict)


if __name__ == '__main__':

    KEYS_LIST_1 = ['1', '2', '3', '4', '5', '6']
    KEYS_LIST_2 = ['1', '2', '3']
    VALUES_LIST = ['one', 'two', 'three', 'four']

    get_dict(KEYS_LIST_1, VALUES_LIST)
    get_dict(KEYS_LIST_2, VALUES_LIST)



