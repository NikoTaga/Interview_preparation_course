
class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Товар - {self.name}, цена - {self.price}'



if __name__ == '__main__':
    a = 'Лошадь'
    b = 2000
    product = ItemDiscountReport(a, b)
    print(product.get_parent_data())