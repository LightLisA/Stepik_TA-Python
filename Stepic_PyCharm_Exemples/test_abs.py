import time
from selenium.webdriver.common.by import By
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    # time.sleep(30) #please uncomment this string for checking
    basket = browser.find_element(By.CLASS_NAME, value='btn-add-to-basket')
    basket.click()

    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    print(x)
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    print(answer)
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
