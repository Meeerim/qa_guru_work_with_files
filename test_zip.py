import zipfile
import os


def test_zip_file():
    path_to_files = 'resources/archive_of_resources.zip'
    files_to_archive = ['eggs.csv', 'docs-pytest-org-en-latest.pdf', 'file_example_XLSX_50.xlsx',
                        'file_example_XLS_10.xls', 'hello.zip']
    with zipfile.ZipFile(path_to_files, 'w', \
                         compression=zipfile.ZIP_DEFLATED) as myzip:
        for file in files_to_archive:
            myzip.write(path_to_files, file)
            print(myzip.namelist())

        assert myzip.namelist() == files_to_archive
