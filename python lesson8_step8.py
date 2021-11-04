from selenium import webdriver
import time , os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    firstName = browser.find_element_by_css_selector("input:nth-child(2)").send_keys("Kekw")
    lastName = browser.find_element_by_css_selector("input:nth-child(4)").send_keys("Ololo")
    email = browser.find_element_by_css_selector("input:nth-child(6)").send_keys("PisyaSisya")



    element = browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_tag_name("button").click()

    print(browser.switch_to.alert.text)
finally:
    time.sleep(5)
    time.sleep(1)
    browser.quit()
