class ProductInput:
    def __init__(self):
        self.name = str(input("Please enter product: "))

    def print_product(self):
        print(f"{self.name}")

    

# test = ProductInput()
# test.print_product()