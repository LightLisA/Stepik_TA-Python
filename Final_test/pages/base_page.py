from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        # Конструктор класса.
        # print(f'BasePage ---- __init__ - {self}')
        # print(f'BasePage ---- __init__ - self.browser --- {browser}')
        self.browser = browser  # :param browser:
        # print(f'BasePage ---- __init__ - self.url ---- {url}')
        self.url = url  # :param url:
        # print(f'BasePage ---- __init__ - self.browser.implicitly_wait === {self.browser.implicitly_wait}')
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    # Если же мы хотим проверить, что какой-то элемент исчезает,
    # то следует воспользоваться явным ожиданием вместе с функцией until_not,
    # в зависимости от того, какой результат мы ожидаем:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print('is_disappeared =====   TimeoutException == 4 sec')
            return False

        return True

    def is_element_present(self, how, what):
        try:
            # print(f'BasePage ----  how - {how}, what - {what}, '
            #       f' self === {self}')
            # print("BasePage ---- is_element_present - find element")
            self.browser.find_element(how, what)
        except NoSuchElementException:
            # print("BasePage ---- is_element_present - except False")
            return False
        # print("BasePage ---- is_element_present - except True")
        return True

    # добавляем абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            # self.browser.find_element(how, what)
            # Нужно ориентироваться на конкретную ситуацию, но общий совет — использовать явные ожидания
            # и Expected Conditions https://selenium-python.readthedocs.io/waits.html
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print('TimeoutException == 4 sec')
            return False

        return True

    def open(self):
        """ Метод открывает нужную страницу, используя метод get()"""
        # print(f'BasePage ---- open - browser.get === {self.browser.get(self.url)}')
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
