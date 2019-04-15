from product_input import ProductInput

class ShoppingList:
    def __init__(self):
        self.shopping_list = []
        self.item = ProductInput()
        
        self.add_item_to_list()

    def add_item_to_list(self):
        self.shopping_list.append(self.item.name)
        self.add_item_choice()

    def add_item_choice(self):
        self.add_item = str(input(f'Would you like to add another item?: ')).upper()

        if self.add_item == "Y" or self.add_item == "YES":
            self.item = ProductInput()

            self.add_item_to_list()

        elif self.add_item == "N" or self.add_item == "NO":
            self.print_shopping_list()

        else:
            print(f'Sorry, unknown response {self.add_item}.')
            self.add_item_choice()

    def print_shopping_list(self):
        print(f'--- Your Shopping List For Today ---')

        for i in range(len(self.shopping_list)):
            print(f'{i}. {self.shopping_list[i]}')

        return self.shopping_list      