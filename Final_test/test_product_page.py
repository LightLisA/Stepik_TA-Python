import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import random


massive = [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="Some Bug")) for i in range(1)]
# massive = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="some bug")), 8, 9])

"""base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
url_list = [base_url + "?promo=offer" + str(n) for n in range(0, 10)]  # promo=offerN has bug, will mark it as xfail
url_list_with_xfail = [pytest.param(url, marks=pytest.mark.xfail) if url[-1] == "N" else url for url in url_list]


@pytest.mark.parametrize('url', url_list_with_xfail)
def test_guest_can_add_product_to_basket(browser, url):
    # функция

Комментарии:
1.  url_list             :    Сначала генерируем список URL страниц
2. url_list_with_xfail   :    Создаем новый список на основе первого, где помечаем URL, на котором тест падает, 
                                как xfail (как в конце этого урока). Не забудьте подставить нужный N :) 
                              Подробнее о методе: Finding and replacing elements in a list - 
                                https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list
3. Запускаем тест!"""


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb"
        page = ProductPage(browser, link)
        reg = LoginPage(browser, link)

        RANDOM_EMAIL = f'testEmail{random.randint(0, 10)}@testmail.com'
        RANDOM_PASSWORD = f'testPassword{random.randint(10, 100)}'

        page.open()
        page.go_to_login_page()
        reg.register_new_user(RANDOM_EMAIL, RANDOM_PASSWORD)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_name_book_and_price()


@pytest.mark.parametrize('ids', massive)
def test_guest_can_add_product_to_basket(browser, ids):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{ids}"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    print(f'browser==== {browser},'
          f'link === {link}')
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_book_and_price()


@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_not_be_success_message()


@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_to_basket()
    page.success_message_should_be_disappeared()


@pytest.mark.regression
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.regression
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.basketchek
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.click_to_view_basket_button()
    page.should_not_be_items_in_basket()
    page.should_be_success_message_basket_empty()



