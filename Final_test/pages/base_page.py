from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math


class BasePage():
    def __init__(self, browser, url, timeout=10):
        # Конструктор класса.
        # print(f'BasePage ---- __init__ - {self}')
        # print(f'BasePage ---- __init__ - self.browser --- {browser}')
        self.browser = browser  # :param browser:
        # print(f'BasePage ---- __init__ - self.url ---- {url}')
        self.url = url  # :param url:
        # print(f'BasePage ---- __init__ - self.browser.implicitly_wait === {self.browser.implicitly_wait}')
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ Метод открывает нужную страницу, используя метод get()"""
        # print(f'BasePage ---- open - browser.get === {self.browser.get(self.url)}')
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            # print(f'BasePage ----  how - {how}, what - {what}, '
            #       f'self === {self}')
            # print("BasePage ---- is_element_present - find element")
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            # print("BasePage ---- is_element_present - except False")
            return False
        # print("BasePage ---- is_element_present - except True")
        return True

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
