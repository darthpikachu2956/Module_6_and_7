class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        print(file.read())
        file.close()

    def add(self, *products):
        for p in products:
            file = open(self.__file_name, 'r')
            prod_list = file.read().splitlines()
            file.close()
            if str(p) in prod_list:
                print(f'The product {p.name} is already on the list.')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{p}\n')
                print(f'The item {p.name} has been added to the list!')
                file.close()


shop1 = Shop()
prod1 = Product('Tomato', 16.1, 'Vegetables')
prod2 = Product('Cabbage', 5.5, 'Vegetables')
prod3 = Product('Cherry', 12.4, 'Berries')
prod4 = Product('Apple', 6.9, 'Fruits')

print(f'{prod1}\n')  # Class Product string check

shop1.get_products()
shop1.add(prod1)
shop1.add(prod2)
shop1.add(prod1)  # Additional try of adding product one
shop1.add(prod3, prod4)
