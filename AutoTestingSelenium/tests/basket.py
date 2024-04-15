import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sitePages.basketPage import BasketPage


def test_basket(driver):
    basket_page = BasketPage(driver)
    basket_page.open("https://arnypraht.com/login/")
    basket_page.basket("ittosole7@mail.ru", "a_mozhet_avtomatom_5?")
    time.sleep(5)
