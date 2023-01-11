# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

# Import "zipfile" module from python
import zipfile

# compress_file definition/function
def compress_file(file_name):

    # Initialize the compression parameters
    with zipfile.ZipFile('test.zip', 'w') as zip:
        # Compress based on the file name provided
        zip.write(file_name)

# decompress_file definition/function
def decompress_file(compressed_file_name):
    
    # Initialize the decompression parameters
    with zipfile.ZipFile(compressed_file_name, 'r') as zip:
        # Decompress the file name provided to a folder named "extracted"
        zip.extractall(path="extracted")

compress_file("testfile.txt")
decompress_file("test.zip")
