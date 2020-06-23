


from selenium import webdriver
import time

link = "https://www.degreesymbol.net/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link2 = browser.find_element_by_link_text("» Degree symbol examples")
    link2.click()
#input1 = browser.find_element_by_tag_name("input")


finally:
    driver.close()
    time.sleep(10)
    browser.quit()
    driver.quit()
