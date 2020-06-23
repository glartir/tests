import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)




finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()