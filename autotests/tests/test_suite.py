import os
import allure
from pages.practice_form_page import PracticeFormPage
from pages.result_table_page import ResultTablePage


@allure.title("Filling out the registration form")
def test_fill_form(browser):
    form_page = PracticeFormPage(browser)
    form_page.open()
    form_page.fill_first_name('Иван')
    form_page.fill_last_name('Иванов')
    form_page.fill_email('ivanov@example.com')
    form_page.select_gender('Male')
    form_page.fill_mobile('8800123123')
    form_page.fill_date()
    form_page.fill_subject()
    form_page.upload_picture(os.path.abspath("../resources/smile.png"))
    form_page.fill_address('г.Иваново, ул.Иванова, д.1')
    form_page.select_state()
    form_page.select_city()
    form_page.click_submit()
    result_page = ResultTablePage(browser)
    title_text = result_page.get_title_text()

    assert title_text == 'Thanks for submitting the form'
