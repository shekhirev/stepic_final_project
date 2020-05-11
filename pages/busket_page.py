from .base_page import BasePage
from .locators import BusketPageLocators

class BusketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BusketPageLocators.ITEMS_IN_BUSKET), \
            "В корзине есть товары, их быть не должно" 

    def should_be_empty_message(self):
        assert self.is_element_present(*BusketPageLocators.EMPTY_BUSKET_MSG), \
            "Нет сообщения, что корзина пустая"