import time

from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def should_be_add_in_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BTN),'Page not have basket btn'

    def add_item_in_basket(self):
        button_item = self.browser.find_element(*ProductPageLocators.PRODUCT_BTN)
        self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        button_item.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(2)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_title_before_click(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def check_price_before_click(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def check_titles(self, title):
        assert title == self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_AFTER).text, f'тайтлы не совпадают {title} =! ' \
                                                                                                  f'{self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_AFTER).text}'

    def check_prices(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AFTER).text, 'цены не совпадают'


