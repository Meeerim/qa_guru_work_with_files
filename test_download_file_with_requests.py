import os.path
import requests
from os_path.os_path_scripts import tmp


def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    file_path = os.path.join(tmp, 'selenium_logo.png')
    r = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(r.content)

    size = os.path.getsize('selenium_logo.png')

    assert size == 30803

