from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketSelector


class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_to_button(*BasketSelector.ADD_TO_BASKET)

    def check_name_book_and_price(self):
        REMEMBER_BOOK_NAME = self.browser.find_element(*BasketSelector.BOOK_NAME).text
        REMEMBER_BOOK_PRICE = self.browser.find_element(*BasketSelector.BOOK_PRICE).text

        BASKET_TOTAL = self.browser.find_element(*BasketSelector.BASKET_TOTAL).text
        BASKET_PRODUCTS = self.browser.find_element(*BasketSelector.BASKET_PRODUCTS).text

        assert REMEMBER_BOOK_NAME == BASKET_PRODUCTS, \
            f'Book name {REMEMBER_BOOK_NAME} is not the equal book in basket {BASKET_PRODUCTS}'
        assert REMEMBER_BOOK_PRICE == BASKET_TOTAL, \
            f'Book Price = {REMEMBER_BOOK_PRICE} is not the same as in basket {BASKET_TOTAL}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"
