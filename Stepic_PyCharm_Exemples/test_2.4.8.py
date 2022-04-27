from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button = browser.find_element_by_id('book')
    button.click()
    
    # проскролить страницу на заданное растояние
    browser.execute_script("window.scrollBy(0, 110);") 
      
    # получить значение Х
    X = browser.find_element_by_id("input_value").text
    
    # посчитать значение чение функции "ln(abs(12*sin(x)))" через  MATH    
    def calc(X):
        return str(math.log(abs(12*math.sin(int(X)))))           
    
    # находим поле для ввода значения
    e_fild = browser.find_element_by_id("answer")
    e_fild.send_keys(calc(X))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()    

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()