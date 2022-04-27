import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    # time.sleep(30) #please uncomment this string for checking
    basket = browser.find_element(By.CLASS_NAME, value='btn-add-to-basket')
    assert basket != None, "The button wasn't found"
