from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
def capcha():
    readnum = browser.find_element_by_id("input_value")
    x = readnum.text
    y = calc(x)

    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button=browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

    button.click()


    #assert "successful" in message.text
    browser.implicitly_wait(5)

    capcha()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()