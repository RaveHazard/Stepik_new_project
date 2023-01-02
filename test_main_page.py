from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest




@pytest.mark.login_guest

class TestLoginFromMainPage():

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.check_empty_total_on_basket_page()
        page.check_empty_basket_text()

