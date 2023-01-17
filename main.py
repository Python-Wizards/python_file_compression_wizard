#!/usr/bin/python
# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

# Declare important program variables
prog_nm="CompressorWiz"
prog_ver="0.1alpha"

# Import front-end framework
import tkinter as gui
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

window = gui.Tk()
window.title(prog_nm+"-("+prog_ver+")")
header = gui.Label(window, text=prog_nm+"-"+prog_ver, height=5, font="Helvetica 20 bold")
header.pack()
button_extract = gui.Button(window, text = "Compress", command = lambda: compress_file("testfile.txt"))
button_extract.pack()
exit_button = gui.Button(window, text='Exit', command=window.destroy)
exit_button.pack()
window.mainloop()

#compress_file("testfile.txt")
#decompress_file("test.zip")
