import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sitePages.editBasketPage import BasketEditionPage

def test_edit_basket(driver):
    basket_editing_page = BasketEditionPage(driver)
    basket_editing_page.open("https://arnypraht.com/login/")
    basket_editing_page.basket_edition("ittosole7@mail.ru", "a_mozhet_avtomatom_5?")
    time.sleep(5)
