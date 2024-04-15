import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from sitePages.firstPage import FirstPage


class FilterPage(FirstPage):
    searchBtn = (By.XPATH, '//*[@class=\"header__main\"]/nav/button')
    filterBtn1 = (By.XPATH, '//*[@class=\"navbar__level\"]/div/ul/li')
    filterBtn2 = (By.XPATH, '//*[@class=\"category__sorting\"]/select/option[3]')



    def filter(self):
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.filterBtn1).click()
        time.sleep(1)
        self.driver.find_element(*self.filterBtn2).click()


