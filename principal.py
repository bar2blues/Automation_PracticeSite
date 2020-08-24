from selenium import webdriver
from Pages.pageIndex import *
from Pages.pageItemList import *
from Pages.pageItem import *
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
        page_item_list = Page_item_list(self.driver)
        page_item = Page_item(self.driver)
        page_index.search_item('dress')
        page_item_list.click_first_item()
        page_item.verify_text('Printed Summer Dress')


    def test_no_items(self):
        page_index = Page_index(self.driver)
        page_index.search_item('computer')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
