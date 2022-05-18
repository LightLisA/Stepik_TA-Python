from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


def test_guest_can_go_to_login_page(browser):
    # print("TEST_MAIN_PAGE --- Link:::")
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    # print("TEST_MAIN_PAGE --- page.open")
    page.open()                      # открываем страницу
    # print("TEST_MAIN_PAGE --- page.go to login page")
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    # print("TEST_MAIN_PAGE --- page.should be login link")
    page.should_be_login_link()

    # login page
    log_in = LoginPage(browser, link)
    # print("TEST_MAIN_PAGE --- log_in.should_be_login_page")
    log_in.should_be_login_page()
    log_in.enter_login_parameters()
    log_in.click_login_button()


@pytest.mark.basketchek
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.click_to_view_basket_button()
    page.should_not_be_items_in_basket()
    page.should_be_success_message_basket_empty()


