from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        name.send_keys("Rozalyn")
        lastname = browser.find_element_by_css_selector(".first_block .second")
        lastname.send_keys("Krozenstaein")
        mail = browser.find_element_by_css_selector(".first_block .third")
        mail.send_keys("roz.kroz@mailer.com")
        # Ваш код, который заполняет не обязательные поля
        phone = browser.find_element_by_css_selector(".second_block .first")
        phone.send_keys("+1659456789809")
        address = browser.find_element_by_css_selector(".second_block .second")
        address.send_keys("UNIT 2 150 NIAGARA LAKE ONTARIO")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(2)
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        welcome_text_elt = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "container")))
        # находим элемент, содержащий текст
        # welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        ER_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(ER_text, welcome_text, "AR is not equal ER 1")
        # ждем чтобы взглянуть
        time.sleep(5)
        # закрываем
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector(".first_block .first")
        name.send_keys("Rozalyn")
        lastname = browser.find_element_by_css_selector(".first_block .second")
        lastname.send_keys("Krozenstaein")
        mail = browser.find_element_by_css_selector(".first_block .third")
        mail.send_keys("roz.kroz@mailer.com")
        # Ваш код, который заполняет не обязательные поля
        phone = browser.find_element_by_css_selector(".second_block .first")
        phone.send_keys("+1659456789809")
        address = browser.find_element_by_css_selector(".second_block .second")
        address.send_keys("UNIT 2 150 NIAGARA LAKE ONTARIO")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        welcome_text_elt = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "container")))
        # находим элемент, содержащий текст
        # welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!12", welcome_text, "AR is not equal ER 1")
        # ждем чтобы взглянуть
        time.sleep(5)
        # закрываем
        browser.quit()


if __name__ == "__main__":
    unittest.main()