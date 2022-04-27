from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
brouser = webdriver.Chrome()
brouser.get(link)

# Заполняем поля
name = brouser.find_element_by_css_selector("input[name='firstname']")
name.send_keys("Bob")
second = brouser.find_element_by_css_selector("input[name='lastname']")
second.send_keys("Sponge")
mulo = brouser.find_element_by_css_selector("input[name='email']")
mulo.send_keys("bob.sponge@gamil_sea.com")

# приатачить файл
current_dir = os.path.abspath(os.path.dirname('/Users/olly1215/Desktop/'))
file_path = os.path.join(current_dir, 'Biography.txt')

# ПРОВЕРКА пути к файлу
# q2 = print(os.path.abspath('Biography.txt'))
# q3 = print(os.path.abspath(os.path.dirname('/Users/olly1215/Desktop/')))
# q4 = print(os.getcwd())

# поиск элемента для загрузки файла
element = brouser.find_element_by_css_selector("#file")
element.send_keys(file_path)

# нажать кнопку Отправить
button = brouser.find_element_by_css_selector("button.btn")
button.click()

# ждем 5 cek чтобы взглянуть
time.sleep(5)

# закрываем
# brouser.close()
brouser.quit()
