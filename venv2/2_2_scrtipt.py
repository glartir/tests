from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
link ="http://suninjuly.github.io/execute_script.html"
browser.get(link)

x=browser.find_element_by_id("input_value")
y=calc(x.text)
input1=browser.find_element_by_id('answer')
input1.send_keys(y)
button=browser.find_element_by_tag_name("button")
browser.execute_script('return arguments[0].scrollIntoView(true);', button)
cbx=browser.find_element_by_id("robotCheckbox")
cbx.click()
rb=browser.find_element_by_id("robotsRule")
rb.click()



#browser.execute_script('return arguments[0].scrollIntoView(true);', button)
button.click()
time.sleep(10)
browser.quit()