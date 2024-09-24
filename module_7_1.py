from os.path import isfile
"""
    Каким образом происходит добавление 2 одинаковый позиций продукта, если проверка осуществляется по его Названию.
    Речь идет о продукте Potato. У них различается только вес, но по условию задачи проверка осуществляется по его
    Названию.
"""
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        if isfile(self.__file_name):
            file = open(self.__file_name, 'r')
            products = file.read()
            file.close()
            return products

    def add(self, *products):
        for product in products:
            if isfile(self.__file_name):
                # if str(product) in self.get_products():  # проверяет всю строку на совпадение
                if product.name in self.get_products():  # проверяет только имя продукта
                    print(f'Продукт {product.name} уже есть в списке')
                else:
                    file = open(self.__file_name, 'a')
                    file.write(str(product) + '\n')
                    file.close()
            else:
                file = open(self.__file_name, 'w')
                file.write(str(product) + '\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')  # разница с 1 продуктом только в весе, проверка по Названию

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
