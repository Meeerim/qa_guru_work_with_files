import os
import time

import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from os_path.os_path_scripts import tmp


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


@pytest.fixture
def browser_setup():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver
    #browser.open("https://github.com/pytest-dev/pytest")
    #browser.element(".d-none .Button-label").click()
    #browser.element('[data-open-app="link"]').click()
    yield
    driver.quit()


def test_file_in_browser(browser_setup):
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(10)
    file_element = os.path.join(tmp, 'pytest-main.zip')
    size_file = os.path.getsize(file_element)
    assert size_file == 1569962

    assert os.path.basename(file_element) == 'pytest-main.zip'