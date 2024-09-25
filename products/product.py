from abc import ABC


class Product(ABC):
    def __init__(self, product_id, product_name, product_retail_price, product_description):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_retail_price = product_retail_price
        self.__product_description = product_description

    # accessors [g, s]
    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_retail_price(self):
        return self.__product_retail_price

    def set_product_retail_price(self, product_retail_price):
        self.__product_retail_price = product_retail_price

    def get_product_description(self):
        return self.__product_description

    def set_product_description(self, product_description):
        self.__product_description = product_description
