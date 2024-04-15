import time
from sitePages.avtorizationPage import avtorizationPage

def test_avtorization(driver):
    login_page = avtorizationPage(driver)
    login_page.open("https://arnypraht.com/login/")
    login_page.login("ittosole7@mail.ru", "a_mozhet_avtomatom_5?")
    time.sleep(5)
    expected_url = "https://arnypraht.com/account/overview/"
    actual_url = login_page.getCurrentUrl()
    assert actual_url == expected_url, f"Провалено"