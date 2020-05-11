from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "В корзине есть товары, их быть не должно" 

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), \
            "Нет сообщения, что корзина пустая"