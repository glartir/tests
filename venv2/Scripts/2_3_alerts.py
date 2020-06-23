import time
import os
import math


from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    readnum = browser.find_element_by_id("input_value")
    x = readnum.text
    y = calc(x)

    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()