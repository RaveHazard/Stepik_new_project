from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REG_FORM = (By.XPATH, '//*[@id="register_form"]')

class ProductPageLocators():
    PRODUCT_BTN = (By.CSS_SELECTOR, 'button.btn-lg:nth-child(3)')
    PRODUCT_TITLE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')
    PRODUCT_PRICE_AFTER = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_TITLE_AFTER = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')

