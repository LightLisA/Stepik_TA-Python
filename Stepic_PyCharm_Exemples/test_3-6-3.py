import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

masiv = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]
final_message = ''


@pytest.mark.parametrize('ids', masiv)
def test_guest_should_see_login_link(browser, ids):
    global final_message
    link = f"https://stepik.org/lesson/{ids}/step/1"
    browser.get(link)

    answer_time = math.log(int(time.time()))

    fild = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area")))
    fild.send_keys(answer_time)
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()
    f1_text = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    get_text = f1_text.text
    #ER_text = "Correct!"
    #assert get_text == ER_text, f"Ожидаемый результат +{ER_text} + не соответствует действительном + {get_text}"
    # МИНУСОМ есть то что ве тесты отмечаются как PASSED # попробовать сделать через Catch raise
    try:
        assert 'Correct!' == get_text
    except AttributeError:
        final_message += get_text  # собираем ответ про Сов с каждой ошибкой
        print(final_message)
