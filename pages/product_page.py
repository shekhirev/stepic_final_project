from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_bucket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BTN), "Кнопки добавить в корзину нет"
        self.browser.find_element(*ProductPageLocators.ADD_BTN).click()
        self.solve_quiz_and_get_code()
    