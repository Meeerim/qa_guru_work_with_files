import os

import pytest
import xlrd

from os_path.os_path_scripts import PROJECT_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

@pytest.fixture
def xls_filepath():
    return os.path.join(PROJECT_ROOT_PATH, '..', 'resources/file_example_XLS_10.xls')

def test_xls_document(xls_filepath):
    book = xlrd.open_workbook(xls_filepath)
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    print(f'Количество строк {sheet.nrows}')
    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}')
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
     print(sheet.row(rx))

    assert book.sheet_names() == ['Sheet1']
    assert book.nsheets >=1
    assert sheet.ncols >=8
    assert sheet.nrows <=10
    assert sheet.cell_value(rowx=2, colx=1) == "Mara"
