from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)

# поджверждаем нажатия на кнопку в confirm попапе
confirm = browser.switch_to.alert
confirm.accept()

# считывает число
input = browser.find_element_by_css_selector("#input_value")
num = input.text

# расчитываем значение
def calc(num):
	return str(math.log(abs(12*math.sin(int(num)))))
	
field = browser.find_element_by_css_selector("input#answer")
field.send_keys(calc(num))

# надимаем на кнопку Отправить
SendButton = browser.find_element_by_css_selector("button.btn")
SendButton.click()

# ждем чтобы взглянуть
time.sleep(5)

# закрываем alert с ответом
alert = browser.switch_to.alert
alert.accept()

# ждем чтобы взглянуть
time.sleep(3)

# закрываем
browser.quit()
