from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from sitePages.firstPage import FirstPage


class avtorizationPage(FirstPage):
    mailInp = (By.XPATH, "//*[@id=\"field-5\"]")
    passwordInp = (By.XPATH, '//*[@id=\"field-6\"]')

    def login(self, email, password):
        self.driver.find_element(*self.mailInp).send_keys(email)
        self.driver.find_element(*self.passwordInp).send_keys(password)
        self.driver.find_element(*self.passwordInp).send_keys(Keys.ENTER)
