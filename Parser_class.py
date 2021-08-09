from bs4 import BeautifulSoup
from Content_class import Content
from selenium import webdriver
#from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time

CHROMEDRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
CHROME_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

chrome_options = Options()
#chrome_options.add_argument("headless")
#chrome_options.add_argument("start-maximized")
#chrome_options.add_argument("incognito")
#chrome_options.add_argument('disable-browser-side-navigation')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.binary_location = CHROME_PATH

class Parser:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        """
        self.driver.header_overrides = {
            #'Accept-Encoding': 'gzip, deflate, br, utf-8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en;q=0.8,en-US;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            #'Content-type': 'application/x-www-form-urlencoded',
            #'Cookie': 'sc=98928D70-904C-4E1E-B020-0AE380000065',
            'Pragma': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        """
    def get_page(self, url):
        self.driver.get(url)
        if len(self.driver.find_elements_by_css_selector("[name=ROBOTS]")) > 0:
            self.driver.get(url)
        time.sleep(5)
        content = self.driver.page_source.encode('utf-8').strip()
        return BeautifulSoup(content, "html.parser")

    def find_content(self, pageObj, selector):
        """
        Utility function used to get a content string from a
        Beautiful Soup object and a selector. Returns an empty
        string if no object is found for the given selector
        """
        selectedElem = pageObj.select_one(selector)
        return selectedElem

    def parse(self, selectorsData, url):
        """
        Extract content from a given page URL
        """
        bs = self.get_page(url)
        if bs is not None:
            store_name = selectorsData.store_name
            product_title = self.find_content(bs, selectorsData.selector_title)
            product_code = self.find_content(bs, selectorsData.selector_code)
            product_price = self.find_content(bs, selectorsData.selector_price)
            product_status = self.find_content(bs, selectorsData.selector_status)

            if product_code != '' and product_title != '' and product_price != '' and product_status != '':
                content = Content(store_name, url, product_title.get_text().strip(), product_code.get_text().strip(), product_price.get_text().strip(), product_status.get_text().strip())

                title = content.get_prod_title()
                code = content.get_prod_code()
                price = content.get_prod_price()
                status = content.get_prod_status()
                return [url, store_name, title, code, price, status]