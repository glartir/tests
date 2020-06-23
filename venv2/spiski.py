import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    readnum1 = browser.find_element_by_id("num1")
    readnum2 = browser.find_element_by_id("num2")
    sum=str(int(readnum1.text)+int(readnum2.text))
    #readnum1 = browser.find_element_by_id("treasure")

    #print(readnum1)
    # Ваш код, который заполняет обязательные поля
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)  # ищем элемент с текстом "Python"

    #input3.send_keys("Sidgmailcom")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()


   # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()