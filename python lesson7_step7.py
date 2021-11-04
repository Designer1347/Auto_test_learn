from selenium import webdriver
import math ,time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radiobutton = browser.find_element_by_id("robotsRule").click()
    buttonCLick = browser.find_element_by_class_name("btn.btn-default").click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(5)
    browser.quit()

