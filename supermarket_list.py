from goto_site import GoToSite

class SupermarketList:
    def __init__(self):
        self.supermarkets = {
            "ASDA":"https://www.asda.com",
            "Tesco":"https://www.tesco.com",
            "Morrisons":"https://groceries.morrisons.com/webshop/startWebshop.do",
            "Iceland":"https://www.iceland.co.uk"
        }

    def supermarket_list(self):
        print(f'Which supermarket would you like to search?')
        print(f'---')

        for name in self.supermarkets:
            print(f'{name}')

        self.open_supermarket()

    def open_supermarket(self):
        self.choice = self.choose_supermarket()

        self.open_browser = GoToSite(self.supermarkets[self.choice])

    def choose_supermarket(self):
        self.query = str(input(": "))

        if self.query in self.supermarkets:
            return self.query
        else:
            self.open_supermarket()


# test = SupermarketList()
# test.supermarket_list()