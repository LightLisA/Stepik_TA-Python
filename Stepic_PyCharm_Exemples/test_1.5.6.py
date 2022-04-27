from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = browser.find_element_by_id("num1").text
    #val1 = .get_attributes(value1)
    
    value2 = browser.find_element_by_id("num2").text
    #val2 = browser.get_attributes(value2)
        
    F_val = str(int(value1) + int(value2))
    #F_val = str(math.fsum([int(value1), int(value2)]))

    # ищем значение в drop-down  списке
    select = Select(browser.find_element_by_tag_name("select"))
    # ищем элемент с текстом полученым в F_val
    select.select_by_value(F_val) 
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()    

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()