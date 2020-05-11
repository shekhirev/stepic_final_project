from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUSKET_LINK = (By.CSS_SELECTOR, '[href="/en-gb/basket/"]')

class MainPageLocators():    
    BASIC_MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    ADD_BTN = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    BUSKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')
    BUSKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner ')
    

class BusketPageLocators():
    EMPTY_BUSKET_MSG = (By.XPATH, '//*[contains(text(), "Your basket is empty")]')
    ITEMS_IN_BUSKET = (By.CSS_SELECTOR,".basket-items")