from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Нажать на кнопку в окне
    fly_button = browser.find_element_by_css_selector("button.btn")
    fly_button.click()
    
    # Запомнить 1ю вкладку
    first_window = browser.window_handles[0]
    
    # Переключиться на новую (ВТОРУЮ) вкладку
    second_window = browser.window_handles[1]
    browser.switch_to_window(second_window)
    
    # получить значение Х
    X = browser.find_element_by_id("input_value").text
    
    # посчитать значение чение функции "ln(abs(12*sin(x)))" через  MATH    
    def calc(X):
        return str(math.log(abs(12*math.sin(int(X)))))           
    
    # находим поле для ввода значения
    e_fild = browser.find_element_by_id("answer")
    e_fild.send_keys(calc(X))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()    

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()