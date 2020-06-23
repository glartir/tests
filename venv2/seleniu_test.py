import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath("//div[1]/div[1]/input")
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_css_selector("div.form-group.second_class input[required]")
    last_name.send_keys('Ivanovich')
    email = browser.find_element_by_class_name("form-control.third")
    email.send_keys('qeqwer@adsf.com')
    #time.sleep(15)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()