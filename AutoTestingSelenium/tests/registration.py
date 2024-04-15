import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sitePages.registrationPage import RegistrationPage


def test_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open("https://arnypraht.com/register/")
    rand = round(random.uniform(1, 99997))
    emai = "kotik_" + str(rand) + "@miu.ru"
    number = "+799743864"+str(round(random.uniform(1, 99)))
    registration_page.registration(emai, "a_mozhet_avtomatom_5?", "girl", number)
    WebDriverWait(driver, 10).until(EC.url_to_be("https://arnypraht.com/register/"))


