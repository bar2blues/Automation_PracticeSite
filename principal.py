from selenium import webdriver
from Pages.pageindex import *
import unittest


class Items(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
       # chrome_options.add_argument('--headless') # no levanta el browser
        self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php')

    def test_view_item_page(self):
        page_index = Page_index(self.driver)
        page_index.search_item('dress')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        title = self.driver.find_element_by_xpath('//h1[@itemprop="name"]').text
        self.assertEqual(title, 'Printed Summer Dress', 'Text should be different')

    def test_no_items(self):
        page_index = Page_index(self.driver)
        page_index.search_item('computer')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
