from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name ("input")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
#input1 = browser.find_element_by_tag_name("input")
finally:

    time.sleep(10)
    browser.quit()
    driver.quit()
    driver.close()