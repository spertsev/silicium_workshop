import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--base-url', action='store', default='https://demoqa.com', help='Base URL the tests'  # default='https://ya.ru'
    )


@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(10)
    url = request.config.getoption('--base-url')
    driver.get(url)
    return driver
