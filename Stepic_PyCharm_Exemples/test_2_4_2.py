from selenium import webdriver
import time
import math
	# подключенеи библиотек для text_to_be_present_in_element 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

	# говорим Selenium проверять , пока значенее не появится
# теория
# Ожидание проверки того, присутствует ли данный текст в указанный элемент. локатор, текст
# class selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
wait = WebDriverWait(browser, 12)
value = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 

button = browser.find_element(By.ID, "book")
button.click()

# считывает число
input = browser.find_element(By.ID, "input_value")
num = input.text

# расчитываем значение
def calc(num):
	return str(math.log(abs(12*math.sin(int(num)))))
	
field = browser.find_element(By.ID, "answer")
field.send_keys(calc(num))

# надимаем на кнопку Отправить
Submit = browser.find_element(By.ID, "solve")
Submit.click()

# ждем чтобы взглянуть
time.sleep(5)

# закрываем
browser.quit()