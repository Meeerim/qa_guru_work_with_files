import os
import csv
from os_path.os_path_scripts import resources

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

csv_filepath =os.path.join(resources,'eggs.csv')


def test_pdf_document():
    with open(csv_filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_filepath) as csvfile:
        csvreader = csv.reader(csvfile)
        data = list(csvreader)
        for row in data:
            print(row)

    assert len(row) == 3
    assert data[0] == ['Anna', 'Pavel', 'Peter']
    assert data[1] == ['Alex', 'Serj', 'Yana']
