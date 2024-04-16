from sitePages.firstPage import FirstPage
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasketPage(FirstPage):
    mailInp = (By.XPATH, "//*[@id=\"field-5\"]")
    passwordInp = (By.XPATH, '//*[@id=\"field-6\"]')
    busketBtn = (By.XPATH, '//*[@class=\"menu__item\"]')
    searchBtn = (By.XPATH, '//*[@class=\"header__main\"]/nav/button')
    filterBtn = (By.XPATH, '//*[@class=\"navbar__level\"]/div/ul/li')
    filterBtn2 = (By.XPATH, "//*[@class=\"cards cards--grid cards--grid-full\"]/div/div[2]/div/form/div/button")
    busketBtn2 = (By.XPATH, '//*[@class=\"header__main\"]/div/ul/li[4]')
    purchaseBtn = (By.XPATH, '//*[@id=\"msOrder\"]')

    def basket(self, email, password):
        self.driver.find_element(*self.mailInp).send_keys(email)
        self.driver.find_element(*self.passwordInp).send_keys(password)
        self.driver.find_element(*self.passwordInp).send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.filterBtn).click()
        self.driver.find_element(*self.filterBtn2).click()



