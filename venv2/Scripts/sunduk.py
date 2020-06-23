import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    readnum = browser.find_element_by_id("treasure")
    x= readnum.get_attribute('valuex')
    print(x)
    y=calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    input4 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    input4.click()
    input3 = browser.find_element_by_css_selector("[id='robotsRule']")
    input3.click()

    #input3.send_keys("Sidgmailcom")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()


   # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()