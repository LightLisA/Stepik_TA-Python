from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# копируем 1e число из строки 
num1 = browser.find_element_by_css_selector("#num1")
get_num1 = num1.text

# копируем 2e число из строки 
num2 = browser.find_element_by_css_selector("#num2")
get_num2 = num2.text

# считаем ответ
sum1 = (int(get_num1) + int(get_num2))
z = str(sum1)


####  ПРоверка суммы ####
#link = "http://suninjuly.github.io/get_attribute.html"
#browser = webdriver.Chrome()
#browser.get(link)

#field1 = browser.find_element_by_css_selector("#answer")
#field1.send_keys(z)

# Ищем значение в drop-dowm list
select1 = Select(browser.find_element_by_tag_name("select"))
select1.select_by_value(z)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# ждем чтобы взглянуть
time.sleep(5)

# закрываем
browser.quit()