class FirstPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def getCurrentUrl(self):
        return self.driver.current_url
