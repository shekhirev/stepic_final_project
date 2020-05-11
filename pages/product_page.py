from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_bucket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BTN), "Кнопки добавить в корзину нет"
        self.browser.find_element(*ProductPageLocators.ADD_BTN).click()
        self.solve_quiz_and_get_code()
        self.check_basket_product_name()
        self.check_basket_price()
        
    def check_basket_price(self):
        price = self.get_product_price(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.get_product_price(*ProductPageLocators.BASKET_PRODUCT_PRICE)        
        assert price == basket_price, "Цена в корзине не совпадает с ценой добавленного товара"
        print(basket_price)

    def check_basket_product_name(self):
        name = self.get_product_name(*ProductPageLocators.PRODUCT_NAME)
        basket_name = self.get_product_name(*ProductPageLocators.BASKET_PRODUCT_NAME)
        assert name == basket_name, "Название товара в корзине не совпадает с добавленным"
        print(basket_name)

    def get_product_price(self, *price):
        return self.browser.find_element(*price).text
    
    def get_product_name(self, *name):
        return self.browser.find_element(*name).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"