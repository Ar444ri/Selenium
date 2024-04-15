from selenium.webdriver.common.by import By
from sitePages.firstPage import FirstPage


class NavigationPage(FirstPage):
    basketBtn = (By.XPATH, '//*[@class=\"menu__item\"]')

    def navigation(self):
        self.driver.find_element(*self.basketBtn).click()
