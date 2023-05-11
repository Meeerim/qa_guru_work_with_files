import os

import pytest
from pypdf import PdfReader

from os_path.os_path_scripts import resources


pdf_filepath = os.path.join(resources, 'docs-pytest-org-en-latest.pdf')


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf_document():
    reader = PdfReader(pdf_filepath)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages >= 1
    assert page is not None
    assert text.__contains__('pytest Documentation')
