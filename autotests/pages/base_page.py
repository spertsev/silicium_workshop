class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.base_url = browser.current_url

    def find(self, *args):
        return self.browser.find_element(*args)
