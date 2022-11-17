from enum import Enum
import random


class ErrorType(Enum):
    id_or_price = 'Product Id or price is not valid'
    product_success = 'Product added successfully'


# will have basic functionality such as a function to add and calculate prices, modify names, adding images and links
class Product:
    def __init__(self, _product_id, title, price, description='', link='', image=''):
        self.product_id = _product_id
        self.title = title
        self.price = price
        self.description = description
        self.link = link
        self.image = image

    @staticmethod
    def _calculate_price():
        return str(round(random.uniform(2.99, 999.99), 2))


def add_prices(self, bulk_data):
    with open(bulk_data) as working_file:
        lines = working_file.read().splitlines()

    with open(bulk_data, 'w') as working_file:
        for line in lines:
            line += ' # ' + self._calculate_price()
            working_file.write(line + '\n')
        working_file.close()


"""
SetUpDb():
will have all the functions related to:
 - setting up the main files (reading it's contents, based on the specific extension); 
 - setting up a backup file and when to make a backup; 
 - find and replace separators and if the case needs it; 
"""


class SetUpDb(Product):
    def __init__(self, title, price, description='', link=''):
        super().__init__(title, price, description, link)

    @staticmethod
    def add_product(bulk_data):
        with open(bulk_data, "r") as intermediary_file:
            for line in intermediary_file:
                __raw_list = line.split(' # ')
                Product._product_id, Product.title, Product.price = __raw_list[0], __raw_list[1], __raw_list[2]
                print(Product._product_id, Product.title, Product.price, end='\n')
        intermediary_file.close()


"""
UpdateDb():
will have all the functions related to:
 - grabbing the existent data and modify it according to user input; 
 - updating the backup file when the case needs it;  
"""


class UpdateDb(Product, SetUpDb):
    def __init__(self, title, price, description='', link=''):
        super().__init__(title, price, description, link)


def testing():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
