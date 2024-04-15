from sitePages.firstPage import FirstPage
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchPage(FirstPage):
    searchBtn = (By.XPATH, '//*[@class=\"sign search-page-invisible\"]')
    searchInput = (By.XPATH, '//*[@class=\"page__pillar\"]/form/div/input')

    def search(self, searchObj):
        self.driver.find_element(*self.searchBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.searchInput).send_keys(searchObj)
        self.driver.find_element(*self.searchInput).send_keys(Keys.ENTER)
