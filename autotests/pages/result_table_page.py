from selenium.webdriver.common.by import By
from pages.base_page import BasePage

title_selector = (By.CSS_SELECTOR, "div[class='modal-title h4']")
table_selector = (By.CSS_SELECTOR, "table")


class ResultTablePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def title(self):
        return self.find(*title_selector)

    def get_title_text(self):
        return self.title().text

    def table(self):
        return self.find(*table_selector)
