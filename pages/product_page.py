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
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_PRICE).text
        assert price == busket_price, "Цена в корзине не совпадает с ценой добавленного товара"
        print(busket_price)

    def check_busket_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        busket_name = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_NAME).text
        assert name == busket_name, "Название товара в корзине не совпадает с добавленным"
        print(busket_name)