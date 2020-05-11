import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.busket_page import BusketPage
from .pages.locators import MainPageLocators
from .pages.locators import ProductPageLocators

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, MainPageLocators.BASIC_MAIN_PAGE_LINK)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, MainPageLocators.BASIC_MAIN_PAGE_LINK)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, MainPageLocators.BASIC_MAIN_PAGE_LINK)
    main_page.open()
    main_page.go_to_busket()
    busket_page = BusketPage(browser, browser.current_url)
    busket_page.should_be_empty()
    busket_page.should_be_empty_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    main_page = MainPage(browser, ProductPageLocators.PRODUCT_PAGE_LINK)
    main_page.open()
    main_page.go_to_busket()
    busket_page = BusketPage(browser, browser.current_url)
    busket_page.should_be_empty()
    busket_page.should_be_empty_message()