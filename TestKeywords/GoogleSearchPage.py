from selenium.webdriver.common.by import By
from TestKeywords.BasePage import BasePage


class GoogleSearchPage(BasePage):

    def __init__(self):
        super().__init__()
        self.search_input = (By.CLASS_NAME, 'gLFyf')
        self.search_button = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        self.accept_cookies_button = (By.ID, 'L2AGLb')

    def open_main_page(self):
        self.open_url('https://www.google.com/')
        # self.get_title() == 'Google'

    def search_for(self, text):
        self.enter_value(self.search_input, text)
        self.do_click(self.search_button)

    def accept_cookies(self):
        self.do_click(self.accept_cookies_button)
