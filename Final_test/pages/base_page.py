from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        # Конструктор класса.
        self.browser = browser          # :param browser:
        self.url = url                  # :param url:
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ Метод открывает нужную страницу, используя метод get()"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
