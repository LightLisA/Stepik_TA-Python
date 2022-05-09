from pages.main_page import MainPage
from pages.login_page import LoginPage


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




