# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

import zipfile

def compress_file(file_name):
    with zipfile.ZipFile('test.zip', 'w') as zip:
        zip.write(file_name)

def decompress_file(compressed_file_name):
    with zipfile.ZipFile(compressed_file_name, 'r') as zip:
        zip.extractall(path="extracted")

compress_file("testfile.txt")
decompress_file("test.zip")
