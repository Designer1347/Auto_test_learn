from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstNumber = browser.find_element_by_id("num1").text
    secondNumber = browser.find_element_by_id("num2").text

    summary = int(firstNumber) + int(secondNumber)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summary))

    button = browser.find_element_by_class_name("btn.btn-default").click()

    print(browser.switch_to.alert.text)
    print("okey")
finally:
    time.sleep(10)
    browser.quit()
