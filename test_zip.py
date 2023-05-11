import zipfile
import os

from os_path.os_path_scripts import resources

zip_filepath = os.path.join(resources, 'archive_of_resources.zip')


def test_zip_file():
    files_to_archive = ['eggs.csv', 'docs-pytest-org-en-latest.pdf', 'file_example_XLSX_50.xlsx',
                        'file_example_XLS_10.xls', 'hello.zip']
    with zipfile.ZipFile(zip_filepath, 'w', \
                         compression=zipfile.ZIP_DEFLATED) as myzip:
        for file in files_to_archive:
            myzip.write(zip_filepath, file)
            print(myzip.namelist())

        assert myzip.namelist() == files_to_archive
