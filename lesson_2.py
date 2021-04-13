
class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Товар - {self.get_name()}, цена - {self.get_price()}'



if __name__ == '__main__':
    a = 'Лошадь'
    b = 2000
    product_par = ItemDiscount(a, b)
    print(product_par.get_name(), product_par.get_price())

    product = ItemDiscountReport(a, b)
    print(product.get_parent_data())