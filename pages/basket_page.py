from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket_button.click()

    def check_empty_total_on_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET_TOTAL), "basket is not empty"

    def check_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert "Your basket is empty" in empty_basket_text.text, 'Basket is not empty'
