import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    readnum = browser.find_element_by_id("input_value")
    x= readnum.text
    y=calc(x)
    input2 = browser.find_element_by_class_name("form-control")
    input2.send_keys(y)
    input4 = browser.find_element_by_id("[for='robotCheckbox']")
    input4.click()
    input3 = browser.find_element_by_css_selector("[for='robotsRule']")
    input3.click()

    #input3.send_keys("Sidgmailcom")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


   # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()