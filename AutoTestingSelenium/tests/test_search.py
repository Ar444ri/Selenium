import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from sitePages.searchPage import SearchPage


def test_search(driver):
    search_page = SearchPage(driver)
    search_page.open("https://arnypraht.com/login/")
    searchObj = "Кто-то лучше Эльвины"
    search_page.search(searchObj)
    time.sleep(10)
    email_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class=\"search-form__info\"]/span"))
    )
    assert email_link.text == "По запросу " + searchObj, f"Failed"