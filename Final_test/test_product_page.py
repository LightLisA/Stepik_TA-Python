import pytest

from pages.product_page import PageObject

masiv = [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason="Some Bug")) for i in range(10)]
# masiv = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="some bug")), 8, 9])

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
