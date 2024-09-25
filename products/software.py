from products.product import Product


class Software(Product):
    def __init__(self,  product_id, product_name, product_retail_price, product_description, license ):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__license = license

    # accessors [g, s]
    def get_license(self):
        return self.__license

    def set_license(self, license):
        self.__license = license

