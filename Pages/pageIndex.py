from selenium.webdriver.common.by import By


class Page_index():

    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, 'search_query_top')
        self.submit_search = (By.NAME, 'submit_search')

    def search_item(self, item):
        self.driver.find_element(*self.search_input).send_keys(item)
        self.driver.find_element(*self.submit_search).click()
        self.driver.implicitly_wait(5)
