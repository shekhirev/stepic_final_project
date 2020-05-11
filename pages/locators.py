from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    BUSKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')
    BUSKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    SUCCESS_MESSAGE = (,)