from selenium.webdriver.common.by import By
import unittest

class Page_item():

    def __init__(self, driver):
        self.driver = driver
        self.title = (By.XPATH, '//h1[@itemprop="name"]')

    def verify_text(self, text_to_verify):
        my_assertion = unittest.TestCase('__init__')
        title = self.driver.find_element(*self.title).text
        my_assertion.assertEqual(title, text_to_verify, 'Text should be different')