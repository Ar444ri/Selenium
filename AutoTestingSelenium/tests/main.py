from tests.basket import test_basket
from tests.editBasket import test_edit_basket
from tests.avtorization import test_avtorization
from tests.registration import test_registration
from tests.navigation import test_navigation
from tests.filter import test_filter
from tests.test_search import test_search
from tests.conftest import driver
from sitePages.basketPage import BasketPage


def test_main ():

    test_avtorization(driver)
    test_registration(driver)
    test_filter(driver)
    test_navigation(driver)
    test_search(driver)
    test_edit_basket(driver)
    test_basket(driver)
