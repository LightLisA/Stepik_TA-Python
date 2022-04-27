from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

elements = browser.find_elements(By.TAG_NAME, "input")
for element in elements:
    element.send_keys("ANYTHING")


button = browser.find_element_by_css_selector("button.btn")
button.click()
