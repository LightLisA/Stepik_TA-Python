from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketSelector():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info>.alertinner>p>strong")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "#messages>div:nth-of-type(1)>.alertinner>strong")


class PageObject(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*BasketSelector.ADD_TO_BASKET).click()

    def check_name_book_and_price(self):
        REMEMBER_BOOK_NAME = self.browser.find_element(*BasketSelector.BOOK_NAME).text
        REMEMBER_BOOK_PRICE = self.browser.find_element(*BasketSelector.BOOK_PRICE).text

        BASKET_TOTAL = self.browser.find_element(*BasketSelector.BASKET_TOTAL).text
        BASKET_PRODUCTS = self.browser.find_element(*BasketSelector.BASKET_PRODUCTS).text

        assert REMEMBER_BOOK_NAME == BASKET_PRODUCTS, f'Book name {REMEMBER_BOOK_NAME} is not the equal book in basket {BASKET_PRODUCTS}'
        assert REMEMBER_BOOK_PRICE == BASKET_TOTAL, f'Book Price = {REMEMBER_BOOK_PRICE} is not the same as in basket {BASKET_TOTAL}'
