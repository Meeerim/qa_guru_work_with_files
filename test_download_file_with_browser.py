import os

import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from os_path.os_path_scripts import CURRENT_FILE_PATH, PROJECT_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp


@pytest.fixture
def browser_setup():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(PROJECT_ROOT_PATH, 'resources'),
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    yield
    driver.quit()


def test_file_in_browser():
    downloaded_file_path = os.path.join(PROJECT_ROOT_PATH, 'tmp','docs-pytest-org-en-latest.pdf')
    assert os.path.basename(downloaded_file_path) == 'docs-pytest-org-en-latest.pdf'