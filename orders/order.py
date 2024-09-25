from datetime import datetime

from orders.order_item import OrderItem


class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__items_list = []
        self.__order_date = datetime.now()        # today date
        self.__order_total = 0.0

    # Accessors G, S : donot create a setter for order_total, items_list
    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_items_list(self):
        return self.__items_list

    def get_order_date(self):
        return self.__order_date

    def get_order_total(self):
        # Loop over the list , calculate sum of attribute ( item_total )
        total = 0
        for item in self.__items_list:
            total = total + item.calc_item_total()
        self.__order_total = total
        return self.__order_total

    # Extra Methods
    def preview_order_receipt(self):
        print('------ Order data ------')
        print('Order id = ', self.__order_id)
        print('Order date = ', self.__order_date)
        print('Customer name = ', self.__customer.get_customer_name())
        print('Order Total = ', self.get_order_total())
        print('----- Order Items List ------')
        for item in self.__items_list:
            print('Line Nbr = ', item.get_line_nbr())
            print('Product name = ',item.get_product().get_product_name())
            print('Quantity = ', item.get_quantity())
            print('Unit price = ', item.calc_unit_price())
            print('Item tax = ', item.calc_item_tax())
            print('Item total = ', item.calc_item_total())
            print('-------')

    def add_product_to_cart(self, new_product):
        # we need to check for new_product ( using product id ) if found before in items_list then +1 to the qty
        # if not found then create new object from OrderItem class and add object to items_list
        is_found = False  # boolean flag
        for item in self.__items_list:
            if new_product.get_product_id() == item.get_product().get_product_id():   # The product is Found in the list
                current_quantity = item.get_quantity()
                item.set_quantity(current_quantity + 1)
                is_found = True
                break

        if is_found == False:       # The product not found before
            item1 = OrderItem(new_product, 1)     # create new object named item1 from class OrderItem
            # fill the list
            self.__items_list.append(item1)



