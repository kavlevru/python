from selenium import webdriver
import time
import unittest

class test_UniqueSelectors1(unittest.TestCase):
    browser = ''
    value = 'some things'
    url = 'http://suninjuly.github.io/registration1.html'
    actual_text = ''
    expected_text = "Congratulations! You have successfully registered!"

    def __init__(self):
        self.browser = webdriver.Chrome()

    def input_values(self):
        self.browser.find_element_by_xpath('//input[contains(@placeholder, "last name") and @required]').send_keys(self.value)
        self.browser.find_element_by_xpath('//input[contains(@placeholder, "first name") and @required]').send_keys(self.value)
        self.browser.find_element_by_xpath('//input[contains(@placeholder, "email") and @required]').send_keys(self.value)

    def send_form(self):
        if self.browser.find_element_by_css_selector("button.btn").click():
            return True

    def actual_text(self):
        return self.browser.find_element_by_tag_name("h1").text

    def test_unique_selectors(self):
        self.browser.get(self.url)
        self.input_values()
        if self.send_form():
            time.sleep(1)
            self.actual_text = self.actual_text()
            if self.actual_text:
                self.assertEqual(self.expected_text, self.actual_text, '')

    def __del__(self):
        self.browser.quit()