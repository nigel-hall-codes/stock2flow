from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from download_driver import DriverBuilder



class StockToFlowScraper:

    def __init__(self):
        self.url = "https://digitalik.net/btc/"
        self.driver = DriverBuilder().get_driver('/Users/nigel/QATesting/venv')

    def open_webpage(self):
        self.driver.get(self.url)

    def parse_page_source(self):
        print(self.driver.page_source)


        print(x)

        print(y)




s = StockToFlowScraper()
s.open_webpage()
time.sleep(3)
s.parse_page_source()
s.driver.close()


