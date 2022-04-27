from selenium import webdriver
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
name = browser.find_element_by_css_selector(".first_block .first")
name.send_keys("Rozalyn")
lastname =  browser.find_element_by_css_selector(".first_block .second")
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
time.sleep(2)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

# ждем чтобы взглянуть
time.sleep(5)

# закрываем
browser.quit()