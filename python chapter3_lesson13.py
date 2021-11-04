from selenium import webdriver
import unittest, time


class test_class_step(unittest.TestCase):

    def test_first(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_required = browser.find_element_by_css_selector("input.first[required]")
        second_required = browser.find_element_by_css_selector("input.second[required]")
        third_required = browser.find_element_by_css_selector("input.third[required]")
        elements = [first_required, second_required, third_required]
        for element in elements:
            element.send_keys("some text")

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
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)
        print("Test passed")

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_required = browser.find_element_by_css_selector("input.first[required]")
        second_required = browser.find_element_by_css_selector("input.second[required]")
        third_required = browser.find_element_by_css_selector("input.third[required]")
        elements = [first_required, second_required, third_required]
        for element in elements:
            element.send_keys("some text")

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
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
