from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from sitePages.firstPage import FirstPage


class RegistrationPage(FirstPage):
    boy = (By.XPATH, '//*[@class=\"fieldset__field field-row choice\"]/label[1]')
    girl = (By.XPATH, '//*[@class=\"fieldset__field field-row choice\"]/label[2]')
    mailInp = (By.XPATH, "//*[@id=\"office-auth-register-email\"]")
    phoneInp = (By.XPATH, '//*[@id=\"office-auth-register-mobilephone\"]')
    passwordInp = (By.XPATH, '//*[@id=\"office-register-form-password\"]')
    dayInp = (By.XPATH, "//*[@class=\"select2-selection select2-selection--single select date-select__day\"]")
    monthInp = (By.XPATH, '//*[@class=\"select2-selection select2-selection--single select date-select__month\"]')
    yearInp = (By.XPATH, '//*[@class=\"select2-selection select2-selection--single select date-select__year\"]')
    randDayInp = (By.XPATH, "//*[@class=\"select2-container select2-container--default select2-container--open\"]/span/span[2]/ul/li")
    randMonthInp = (By.XPATH, "//*[@class=\"select2-container select2-container--default select2-container--open\"]/span/span[2]/ul/li")
    randYearInp = (By.XPATH,
                   "//*[@class=\"select2-container select2-container--default select2-container--open\"]/span/span["
                   "2]/ul/li[25]")
    privatePolicy = (By.XPATH, '//*[@class=\"checkbox checkbox--basic checkbox--s checkbox--policy\"]/span[1]')
    registrationBtn = (
    By.XPATH, '//*[@class=\"bar__button button button--solid button-loader button-loader--reg-submit\"]')

    def select_gender(self, gender):
        if gender == "boy":
            self.driver.find_element(*self.boy).click()
        elif gender == "girl":
            self.driver.find_element(*self.girl).click()
        else:
            raise ValueError("В России только 2 пола!")

    def registration(self, email, password, gender, mobile):
        self.select_gender(gender)
        self.driver.find_element(*self.mailInp).send_keys(email)
        self.driver.find_element(*self.mailInp).send_keys(Keys.ENTER)
        self.driver.find_element(*self.passwordInp).send_keys(password)
        self.driver.find_element(*self.phoneInp).send_keys(mobile)

        self.driver.find_element(*self.dayInp).click()
        self.driver.find_element(*self.randDayInp).click()
        self.driver.find_element(*self.monthInp).click()
        self.driver.find_element(*self.randMonthInp).click()
        self.driver.find_element(*self.yearInp).click()
        self.driver.find_element(*self.randYearInp).click()

        self.driver.find_element(*self.privatePolicy).click()
        self.driver.find_element(*self.registrationBtn).click()
