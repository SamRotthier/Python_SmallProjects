import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

#New Way:
#In the new way you also don't have to install the chromedriver
#driver = webdriver.Chrome()
#driver.get('https://google.com')
#time.sleep(5)
#print(driver.title)

#The old way:
#Here you do need to install the chromedriver -> https://googlechromelabs.github.io/chrome-for-testing/#stable
driver_exe = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')

class Browser:
    def __init__(self, driver: str):
        print('starting up...')
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        print(f'Opening {url}')
        self.browser.get(url)

#In new version you don't need the close browser def (now it terminates the browser when script is finished)
    def close_browser(self):
        print('Closing browser...')
        self.browser.close()

if __name__ == '__main__':
    browser = Browser(driver_exe)

    browser.open_page('https://www.python.org')
    time.sleep(5) 

    browser.close_browser
    time.sleep(5)