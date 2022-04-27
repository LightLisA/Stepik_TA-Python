from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# копируем число из строки
box = browser.find_element_by_css_selector("#treasure")
number = box.get_attribute("valuex")

# Посчитать математическую функцию
def calc(number):
  return str(math.log(abs(12*math.sin(int(number)))))

# Ввести ответ в текстовое поле
y = calc(number)
field1 = browser.find_element_by_css_selector("#answer")
field1.send_keys(y)

# Отметить checkbox "Подтверждаю, что являюсь роботом"
checkbox1 = browser.find_element_by_css_selector("#robotCheckbox")
checkbox1.click()

# Отметить checkbox "Подтверждаю, что являюсь роботом"
checkbox1 = browser.find_element_by_css_selector("#robotsRule")
checkbox1.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# ждем чтобы взглянуть
time.sleep(5)

# закрываем
browser.quit()