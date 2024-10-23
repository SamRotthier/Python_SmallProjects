import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#New Way:
#In the new way you also don't have to install the chromedriver
driver = webdriver.Chrome()
driver.get('https://google.com')
time.sleep(5)
print(driver.title)

#The old way:
#Here you do need to install the chromedriver
#class Browser:
#    def __init__(self, driver: str):
#        print('starting up...')
#        self.service = Service(driver)
#        self.browser = webdriver.Chrome(service=self.service)

#    def open_page(self, url: str):
#        print(f'Opening {url}')
#        self.browser.get(url)

#    def close_browser(self):
#        print('Closing browser...')
#        self.browser.close()

#if __name__ == '__main__':
#    browser = Browser('chromedriver')

#    browser.open_page('https://www.python.org')
#    time.sleep(5) 