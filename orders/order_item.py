from products.hardware import Hardware
from taxable.taxable import Taxable


class OrderItem:
    # static attributes
    __static_line_nbr = 1

    def __init__(self, product, quantity):
        self.__line_nbr = OrderItem.__static_line_nbr         # int
        OrderItem.__static_line_nbr = OrderItem.__static_line_nbr + 1   # to make the static attribute like a serial
        self.__product = product    # Object from Product class
        self.__quantity = quantity      # int

    # Accessors G, S
    def get_line_nbr(self):
        return self.__line_nbr

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    # donot create a setter to line_nbr

    # Extra Methods
    def calc_unit_price(self):
        return self.__product.get_product_retail_price()

    def calc_item_tax(self):    # Polymorphism
        if isinstance(self.__product, Taxable):
            # i need to call the get_tax(amount) function from Hardware class
            amount = self.calc_unit_price() * self.__quantity
            return self.__product.get_tax(amount)
        else:
            return 0

    def calc_item_total(self):
        return self.calc_unit_price() * self.__quantity + self.calc_item_tax()