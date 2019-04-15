from selenium import webdriver

# Location of webdriver, in this instance we are using Chrome
DRIVER_LOCATION = "bin/chromedriver"

class GoToSite:
    def __init__(self, address):
        self.address = address
        self.driver = webdriver.Chrome(DRIVER_LOCATION)
        self.driver.get(self.address)
