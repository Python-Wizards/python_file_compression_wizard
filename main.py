#!/usr/bin/python
# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

# Import "zipfile" module from python
import zipfile

# compress_file definition/function
def compress_file(filenm):
    # Initialize the compression parameters
    with zipfile.ZipFile('test.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
        # Compress based on the file name provided
        zip.write(filenm)
# decompress_file definition/function
def decompress_file(compressed_filenm):
    
    # Initialize the decompression parameters
    with zipfile.ZipFile(compressed_filenm, 'r') as zip:
        # Decompress the file name provided to a folder named "extracted"
        zip.extractall(path="extracted")

#compress_file("testfile.txt")
#decompress_file("test.zip")
