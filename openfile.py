class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self) -> str:
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''  # Возврат пустой строки, если файл не найден.

    def add(self, *products: Product):
        current_products = self.get_products().strip().split('\n')
        current_names = {product.split(', ')[0] for product in current_products if product}

        for product in products:
            if product.name in current_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')

if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Выводит: Spaghetti, 3.4, Groceries


    s1.add(p1, p2, p3)


    print(s1.get_products())




