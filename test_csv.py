import os
import csv
import pytest
from os_path.os_path_scripts import PROJECT_ROOT_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

@pytest.fixture
def csv_filepath():
    return os.path.join(PROJECT_ROOT_PATH, '..', 'resources/eggs.csv')


def test_pdf_document(csv_filepath):
    with open(csv_filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open('resources/eggs.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
        for row in data:
            print(row)

    assert len(row) == 3
    assert data[0] == ['Anna', 'Pavel', 'Peter']
    assert data[1] == ['Alex', 'Serj', 'Yana']
