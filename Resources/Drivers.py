from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager


class Drivers:

    def __init__(self):
        self.drivers = []

    def install_list_of_browsers(self, list_of_browsers):
        for browser in list_of_browsers:
            if browser == "Chrome":
                self.install_chrome()
            if browser == "Edge":
                self.install_edge()
            if browser == "Firefox":
                self.install_firefox()

        return self.drivers

    def install_chrome(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        self.drivers.append(driver)

    def install_firefox(self):
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        self.drivers.append(driver)

    def install_edge(self):
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        self.drivers.append(driver)
