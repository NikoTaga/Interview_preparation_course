
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

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__name = name
        self.__price = price
        self.__discount = discount

    def calc_disc_price(self):
        return self.get_price() - self.get_price() * 0.01 * self.__discount

    def __str__(self):
        return f'Товар - {self.get_name()}, цена - {self.calc_disc_price()}'

    def get_parent_data(self):
        return self.__str__()

    def get_info(self):
        return f'Наименование - {self.get_name()}'


class ItemDiscountReport1(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__name = name
        self.__price = price
        self.__discount = discount

    def calc_disc_price(self):
        return self.get_price() - self.get_price() * 0.01 * self.__discount

    def __str__(self):
        return f'Товар - {self.get_name()}, цена - {self.calc_disc_price()}'

    def get_parent_data(self):
        return self.__str__()

    def get_info(self):
        return f'Цена - {self.get_price()}'



if __name__ == '__main__':
    a = 'Лошадь'
    b = 2000
    product_par = ItemDiscount(a, b)
    print(product_par.get_name(), product_par.get_price())
    print(product_par)
    print('--------')

    a = 'Кабан'
    b = 3000
    d = 15
    product = ItemDiscountReport(a, b, d)
    print(product.get_name(), product.get_price())
    print(product.get_parent_data())
    print('--------')

    print(product.get_info())

    product1 = ItemDiscountReport(a, b, d)
    print(product1.get_info())

    product_list = [product, product1]
    for i in product_list:
        print(i.get_info())