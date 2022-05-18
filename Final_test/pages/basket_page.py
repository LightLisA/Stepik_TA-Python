from .base_page import BasePage
from .locators import BasketSelector


class BasketPage(BasePage):
    def click_to_view_basket_button(self):
        self.click_to_button(*BasketSelector.VIEW_BASKET_BUTTON)

    def should_be_success_message_basket_empty(self):
        assert self.is_element_present(*BasketSelector.MESSAGE_BASKET_EMPTY), \
            'Basket is not empty'

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketSelector.ITEMS_IN_BASKET), \
            "Items are presented in basket, but they should not be"
