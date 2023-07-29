from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:

    # Locators
    class_page_title = 'title'

    # Services

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()

    def is_url_page(self, url):
        return self.driver.current_url == url

    def has_page_title(self, title_text):
        page_title = self.driver.find_element(By.CLASS_NAME, self.class_page_title).text
        return page_title == title_text

    def check_page(self, url, title_text):
        return self.is_url_page(url) and self.has_page_title(title_text)
