import os
import sys

from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver as chrome_webdriver
from selenium.webdriver import Proxy

from pyvirtualdisplay import Display


class DriverBuilder():

    def get_driver(self, download_location=None, headless=False):

        driver = self._get_chrome_driver(download_location, headless)

        driver.set_window_size(5000, 5000)

        return driver

    def _get_chrome_driver(self, download_location, headless):
        chrome_options = chrome_webdriver.Options()
        if download_location:
            prefs = {'download.default_directory': download_location,
                     'download.prompt_for_download': False,
                     'download.directory_upgrade': True,
                     'safebrowsing.enabled': False,
                     'safebrowsing.disable_download_protection': True}

            chrome_options.add_experimental_option('prefs', prefs)

        if headless and not os.path.isdir("/home/nhall/selpyvenv/"):
            chrome_options.add_argument("--headless")

        if os.path.isdir("/home/nhall/selpyvenv/"):
            display = Display(visible=0, size=(800, 600))
            display.start()

            chrome_options.add_argument("--no-sandbox")

            driver = Chrome(chrome_options=chrome_options, executable_path="/usr/bin/chromedriver")
            # chrome_options.add_argument("--disable-gpu")

        else:
            driver = Chrome(chrome_options=chrome_options, executable_path="/Users/nigel/AuthnetTests/chromedriver 4")

        if headless:
            self.enable_download_in_headless_chrome(driver, download_location)

        return driver

    def enable_download_in_headless_chrome(self, driver, download_dir):
        """
        there is currently a "feature" in chrome where
        headless does not allow file download: https://bugs.chromium.org/p/chromium/issues/detail?id=696481
        This method is a hacky work-around until the official chromedriver support for this.
        Requires chrome version 62.0.3196.0 or above.
        """

        # add missing support for chrome "send_command"  to selenium webdriver
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = driver.execute("send_command", params)

