from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #print("should_be_login_url complite")
        assert "login" in self.browser.current_url, 'Login not contains in current url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        #print("should_be_login_form complite")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        #print("should_be_register_form complite")
        assert self.is_element_present(*LoginPageLocators.REG_FORM)
