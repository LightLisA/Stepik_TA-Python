import pytest

from pages.product_page import PageObject

masiv = [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="Some Bug")) for i in range(10)]
# masiv = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="some bug")), 8, 9])
"""product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
bad_links = [7] #допустим падают тесты 1 и 2
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10) if no not in bad_links]
bad_urls = [f"{product_base_link}/?promo=offer{no}" for no in bad_links]


@pytest.mark.parametrize('ids', urls+list(map(lambda mn: \
pytest.param(mn, marks=pytest.mark.xfail(strict=True)), bad_urls)))"""

@pytest.mark.parametrize('ids', masiv)
def test_guest_can_add_product_to_basket(browser, ids):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{ids}"
    page = PageObject(browser,
                      link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    print(f'browser==== {browser},'
          f'link === {link}')
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_book_and_price()
