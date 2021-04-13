
class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __str__(self):
        return f'Товар - {self.get_name()}, цена - {self.get_price()}'


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price):
        super().__init__(name, price)
        self.__name = name
        self.__price = price

    def get_parent_data(self):
        return f'Товар - {self.get_name()}, цена - {self.get_price()}'



if __name__ == '__main__':
    a = 'Лошадь'
    b = 2000
    product_par = ItemDiscount(a, b)
    print(product_par.get_name(), product_par.get_price())
    print(product_par)
    print('--------')

    a = 'Кабан'
    b = 3000
    product = ItemDiscountReport(a, b)
    print(product.get_name(), product.get_price())
    print(product.get_parent_data())