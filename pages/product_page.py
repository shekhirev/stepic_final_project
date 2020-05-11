from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_bucket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BTN), "Кнопки добавить в корзину нет"
        self.browser.find_element(*ProductPageLocators.ADD_BTN).click()
        self.solve_quiz_and_get_code()
        self.check_busket_product_name()
        self.check_busket_price()
        
    def check_busket_price(self):
        price = self.get_product_price(*ProductPageLocators.PRODUCT_PRICE)
        busket_price = self.get_product_price(*ProductPageLocators.BUSKET_PRODUCT_PRICE)        
        assert price == busket_price, "Цена в корзине не совпадает с ценой добавленного товара"
        print(busket_price)

    def check_busket_product_name(self):
        name = self.get_product_name(*ProductPageLocators.PRODUCT_NAME)
        busket_name = self.get_product_name(*ProductPageLocators.BUSKET_PRODUCT_NAME)
        assert name == busket_name, "Название товара в корзине не совпадает с добавленным"
        print(busket_name)

    def get_product_price(self, *price):
        return self.browser.find_element(*price).text
    
    def get_product_name(self, *name):
        return self.browser.find_element(*name).text