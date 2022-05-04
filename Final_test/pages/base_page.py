class BasePage():
    def __init__(self, browser, url):
        # Конструктор класса.
        self.browser = browser          # :param browser:
        self.url = url                  # :param url:

    def open(self):
        """ Метод открывает нужную страницу, используя метод get()"""
        self.browser.get(self.url)
