
class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Товар - {self.__name}, цена - {self.__price}'



if __name__ == '__main__':
    a = 'Лошадь'
    b = 2000
    product_par = ItemDiscount(a, b)
    print(product_par.name, product_par.price)

    product = ItemDiscountReport(a, b)
    print(product.get_parent_data())