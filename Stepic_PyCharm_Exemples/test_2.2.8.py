from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполнить текстовые поля: имя, фамилия, email
    name = browser.find_element_by_name('firstname')
    name.send_keys("Rozalyn")
    lastname =  browser.find_element_by_name('lastname')
    lastname.send_keys("Krozenstaein")
    mail = browser.find_element_by_name('email')
    mail.send_keys("roz.kroz@mailer.com")
    
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    file_b = browser.find_element_by_id("file")
    # получаем путь к директории текущего исполняемого файла 
    # - чтобы выяснить в какую директорию ложить файл выполните в отдельном файле:
    #import os 
    #print(os.path.abspath(os.path.dirname(__file__)))
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file_1.txt')         
    file_b.send_keys(file_path)        
    
    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()    

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()