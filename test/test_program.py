from customers.company import Company
from orders.order import Order
from products.hardware import Hardware
from products.manual import Manual
from products.software import Software

# create products objects [ hardware, software, manual ]
my_keyboard = Hardware(1, 'Keyboard assus', 70, 'Accessories', 3)
my_office = Software(2, 'Office 2024', 300, 'Ms. Office', '1232-1231-1231')
my_magazine = Manual(3, 'IT Magazine', 50, 'Newspapers', 'El Ahram')
my_printer = Hardware(4, 'Xerox Printer', 2000, 'Printers', 10)
my_scanner = Hardware(5, 'Cannon Scanner', 3000, 'Scanners', 7)

# Create Customers [ Company - individual ]
raya_company = Company(100, 'Raya Co.', '0101654879', 'Cairo - Egypt', 'Ahmed Aly', 10)
vodafone_company = Company(101, 'Vodafone Egypt', '0101231211', 'Maadi - Egypt', 'Ola', 20)

# Create Orders
order1001 = Order(1001, raya_company)
# add products to order
order1001.add_product_to_cart(my_office)
order1001.add_product_to_cart(my_office)
order1001.add_product_to_cart(my_printer)
order1001.add_product_to_cart(my_printer)
order1001.add_product_to_cart(my_printer)
order1001.add_product_to_cart(my_scanner)
order1001.add_product_to_cart(my_scanner)
order1001.add_product_to_cart(my_scanner)
order1001.add_product_to_cart(my_scanner)
order1001.add_product_to_cart(my_keyboard)

# hw tasks
"""
order1001.add_product_qty_to_cart(my_printer, 4)  # add 4 units
order1001.remove_product_from_cart(my_keyboard)  # remove 1 unit
order1001.remove_product_from_cart(my_printer, 3)  # remove 3 units
"""

# preview receipt
order1001.preview_order_receipt()



