import sys
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

first_name_selector = (By.CSS_SELECTOR, "#firstName")
last_name_selector = (By.XPATH, "//input[@placeholder='Last Name']")
email_selector = (By.ID, "userEmail")
radio_male_selector = (By.CSS_SELECTOR, ".custom-radio:nth-child(1) > .custom-control-label")
radio_female_selector = (By.CSS_SELECTOR, ".custom-radio:nth-child(2) > .custom-control-label")
radio_other_selector = (By.CSS_SELECTOR, ".custom-radio:nth-child(3) > .custom-control-label")
mobile_selector = (By.CSS_SELECTOR, "input[placeholder='Mobile Number'")
date_selector = (By.CSS_SELECTOR, "#dateOfBirthInput")
calendar_date_selector = (By.CSS_SELECTOR, ".react-datepicker__day--028:nth-child(1)")
subject_selector = (By.CSS_SELECTOR, "#subjectsInput")
math_subject_selector = (By.CSS_SELECTOR, "#react-select-2-option-0")
picture_selector = (By.CSS_SELECTOR, "#uploadPicture")
address_selector = (By.CSS_SELECTOR, "textarea[placeholder='Current Address']")
state_selector = (By.XPATH, "//*[contains(text(),'Select State')]")
first_state_selector = (By.CSS_SELECTOR, "#react-select-3-option-0")
city_selector = (By.XPATH, "//*[contains(text(),'Select City')]")
first_city_selector = (By.CSS_SELECTOR, "#react-select-4-option-0")
submit_selector = (By.CSS_SELECTOR, "#submit")


class PracticeFormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(f'{self.base_url}automation-practice-form')

    def first_name(self):
        return self.find(*first_name_selector)

    def fill_first_name(self, text):
        self.first_name().send_keys(text)

    def last_name(self):
        return self.find(*last_name_selector)

    def fill_last_name(self, text):
        self.last_name().send_keys(text)

    def email(self):
        return self.find(*email_selector)

    def fill_email(self, text):
        self.email().send_keys(text)

    def radio_male(self):
        return self.find(*radio_male_selector)

    def radio_female(self):
        return self.find(*radio_female_selector)

    def radio_other(self):
        return self.find(*radio_other_selector)

    def select_gender(self, gender):
        if gender == 'Male':
            self.radio_male().click()
        elif gender == 'Female':
            self.radio_female().click()
        elif gender == 'Other':
            self.radio_other().click()
        else:
            raise Exception("Not supported gender")

    def mobile(self):
        return self.find(*mobile_selector)

    def fill_mobile(self, number_string):
        self.mobile().send_keys(number_string)

    def date(self):
        return self.find(*date_selector)

    def calendar_date(self):
        return self.find(*calendar_date_selector)

    def fill_date(self):
        self.date().click()
        self.calendar_date().click()

    def subject(self):
        return self.find(*subject_selector)

    def math_subject(self):
        return self.find(*math_subject_selector)

    def fill_subject(self):
        self.subject().send_keys('m')
        self.math_subject().click()

    def picture(self):
        return self.find(*picture_selector)

    def upload_picture(self, path_string):
        self.picture().send_keys(path_string)

    def address(self):
        return self.find(*address_selector)

    def fill_address(self, text):
        self.address().send_keys(text)

    def state(self):
        return self.find(*state_selector)

    def first_state(self):
        return self.find(*first_state_selector)

    def select_state(self):
        self.state().click()
        self.first_state().click()

    def city(self):
        return self.find(*city_selector)

    def first_city(self):
        return self.find(*first_city_selector)

    def select_city(self):
        self.city().click()
        self.first_city().click()

    def submit(self):
        return self.find(*submit_selector)

    def click_submit(self):
        for i in range(1, 11):
            try:
                self.submit().click()
            except Exception as e:
                print(sys.exc_info())
                time.sleep(2)
                continue
            break
