from selenium.webdriver.common.by import By


class BasketSelector:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # Работа с элементами внутри Корзины
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info>.alertinner>p>strong")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "#messages>div:nth-of-type(1)>.alertinner>strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".content>#content_inner>form")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, ".content>div>p")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>span>a")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-of-type(2)>.alertinner")
