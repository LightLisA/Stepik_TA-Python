from pages.product_page import PageObject


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

    print(f'browser==== {browser},'
          f'link === {link}')
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_book_and_price()