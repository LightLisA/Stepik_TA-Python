from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# копируем число из строки
x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text

# Посчитать математическую функцию от X
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Ввести ответ в текстовое поле
y = calc(x)
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