from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resources.Drivers import Drivers


# Parent class for all pages

class BasePage(Drivers):

    def __init__(self):
        super().__init__()
        if self.drivers:
            self.get_driver()
        else:
            self.driver = None

    def get_driver(self):
        if self.drivers:
            self.driver = self.drivers.pop()

    def open_url(self, url):
        self.driver.get(url)

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_value(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_element_value(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def go_back_browser(self):
        self.driver.back()
