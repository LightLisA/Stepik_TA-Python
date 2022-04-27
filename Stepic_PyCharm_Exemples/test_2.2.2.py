from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # получить значение Х
    X = browser.find_element_by_id("input_value").text
    
    # посчитать значение чение функции "ln(abs(12*sin(x)))" через  MATH    
    def calc(X):
        return str(math.log(abs(12*math.sin(int(X)))))
    
    # проскролить страницу до кнопки Submit
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)    
    # проскролить страницу на заданное растояние
    browser.execute_script("window.scrollBy(0, 110);")            
    
    # находим поле для ввода значения
    e_fild = browser.find_element_by_id("answer")
    e_fild.send_keys(calc(X))
        
    # Поиск элемента из выпадающего списка
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(F_val) 
    
    # Выбрать checkbox "I'm the robot".
    o_checkbox = browser.find_element_by_id("robotCheckbox")
    o_checkbox.click()
    
    # Переключить radiobutton "Robots rule!".
    o_radiobutton = browser.find_element_by_id("robotsRule")
    o_radiobutton.click()        
    
    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element_by_css_selector('[type="submit"')
    button.click()    

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()