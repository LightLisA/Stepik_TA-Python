from selenium import webdriver
import math
import time

# открываем линку
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# нажымаем на кнопку "Хочу отправиться в волшебное путешествие"
want_to = browser.find_element_by_css_selector("button.trollface.btn")
want_to.click()

# запоминае парет табу
first_window = browser.window_handles[0]

# переходим на другую табу
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

# считуем число
num = browser.find_element_by_css_selector("span#input_value")
x = num.text

# расчитываем значение
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)	
field = browser.find_element_by_css_selector("input#answer")
field.send_keys(y)

# надимаем на кнопку Отправить
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)

# закрываем попап
popup = browser.switch_to.alert
popup.accept()

time.sleep(3)

# закрываем первую вкладку
browser.switch_to.window(first_window)
browser.close()

time.sleep(3)

# закрываем броузер
browser.quit() 