from selenium import webdriver


class PageObject:

    # Services

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

    def close(self):
        self.driver.quit()
