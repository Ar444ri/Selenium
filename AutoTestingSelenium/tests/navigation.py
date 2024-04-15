import time

from sitePages.navigationPage import NavigationPage

def test_navigation(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.open("https://arnypraht.com/login/")
    navigation_page.navigation()
    time.sleep(5)
    expected_url = "https://arnypraht.com/cart/"
    actual_url = navigation_page.getCurrentUrl()
    assert actual_url == expected_url, f"Все супер"