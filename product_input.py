class ProductInput:
    def __init__(self):
        self.product = input("Please enter product: ")

    def product_input(self):
        return self.product

    def print_product(self):
        print(f"You are searching for {self.product}, is that correct?")

test = ProductInput()
test.product_input()
test.print_product()