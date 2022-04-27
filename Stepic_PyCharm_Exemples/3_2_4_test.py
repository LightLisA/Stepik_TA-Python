import unittest
from selenium import webdriver
import time

browser = webdriver.Chrome()

class TestStepik(unittest.TestCase):
	def test_form_1(self):
		f1_link = "http://suninjuly.github.io/registration1.html"
		browser.get(f1_link)

		# Ваш код, который заполняет обязательные поля
		f1_name = browser.find_element_by_css_selector(".first_block .first")
		f1_name.send_keys("Rozalyn")
		f1_lastname =  browser.find_element_by_css_selector(".first_block .second")
		f1_lastname.send_keys("Krozenstaein")
		f1_mail = browser.find_element_by_css_selector(".first_block .third")
		f1_mail.send_keys("roz.kroz@mailer.com")

		# Ваш код, который заполняет не обязательные поля
		f1_phone = browser.find_element_by_css_selector(".second_block .first")
		f1_phone.send_keys("+1659456789809")
		f1_address = browser.find_element_by_css_selector(".second_block .second")
		f1_address.send_keys("UNIT 2 150 NIAGARA LAKE ONTARIO")

		# Отправляем заполненную форму
		f1_button = browser.find_element_by_css_selector("button.btn")
		f1_button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		browser.implicitly_wait(10)		

		# находим элемент, содержащий текст
		f1_welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		f1_welcome_text = f1_welcome_text_elt.text

		# запоминаем 1ю вкладку
		first_window = browser.window_handles[0]

		# проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		f1_ER = 'Congratulations! You have successfully registered!'
		self.assertEqual(f1_ER, f1_welcome_text, "First ER is not match")


	def test_form_2(self):
		# открываем 2ю вкладку	
		browser.execute_script("window.open('http://suninjuly.github.io/registration2.html')")
		# запоминаем 2ю вкладку
		second_window = browser.window_handles[1]
		# переходим на 2ю вкладку
		browser.switch_to.window(second_window)

		# заполняет обязательные поля
		f2_name = browser.find_element_by_css_selector(".first_block .first")
		f2_name.send_keys("Rosa")

		f2_email = browser.find_element_by_css_selector(".first_block .third")
		f2_email.send_keys("rosa.wil@cogery.com")

		# Заполняет не обязательные поля
		f2_phone = browser.find_element_by_css_selector(".second_block .first")
		f2_phone.send_keys("+875456212001")

		f2_address = browser.find_element_by_css_selector(".second_block .second")
		f2_address.send_keys("42 SYSCON ROAD WILLYAMS")

		# НАжимаем Отправить форму
		f2_button = browser.find_element_by_css_selector("button.btn")
		f2_button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		browser.implicitly_wait(10)

		# находим элемент, содержащий текст
		f2_text_elm = browser.find_element_by_css_selector(".container h1")
		f2_text = f2_text_elm.text

		# ждем чтобы взглянуть
		time.sleep(5)

		# с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		f2_ER = 'Congratulations! You have successfully registered!'
		self.assertEqual(f2_ER, f2_text, "Second ER is not match")

# закрываем
# browser.switch_to.window(first_window)
# browser.close() 
# browser.quit()

	# def test_compare(self):
	# 	self.assertEqual(f1_welcome_text, f2_text, "ERs are not match")

if __name__ == "__main__":
    unittest.main()

