import time

from sitePages.filterPage import FilterPage

def test_filter (driver):
    filter_page = FilterPage(driver)
    filter_page.open("https://arnypraht.com/login/")
    filter_page.filter()
    time.sleep(5)