#!/usr/bin/python
# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

# Declare important program variables
prog_nm="CompressorWiz"
prog_ver="0.2Beta"

# Import front-end framework
import customtkinter as gui
import tkinter as gui_legacy
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
# Import "zipfile" and "os" module from python
import zipfile                                                                                     
import os

# Set GUI theme
gui.set_appearance_mode("dark")
gui.set_default_color_theme("dark-blue")
filesrc=""
filenm=""
zipnm=""
levels = 9

def file_browser(event=None):
    frame_status.configure(text="No action selected.\n\n\n")
    global filesrc, filenm, zipnm
    filesrc = askopenfilename()
    filenm = filesrc.split('/')[len(filesrc.split('/'))-1]
    zipnm = os.path.splitext(filenm)[0]+".zip"
    if filenm=="":
        frame_filestatus.configure(text="No file selected.")
    else:
        frame_filestatus.configure(text="To compress : "+filenm)
        frame_filestatus.grid(pady=8)

# compress_file definition/function
def compress_file(filesrc):
    # Initialize the compression parameters
    with zipfile.ZipFile(zipnm, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=levels) as zip:
        # Compress based on the file name provided
        zip.write(filesrc, arcname=filenm)
        # display original file size definition/function
        def display_filesize(filesrc):
            ogfilesize = (os.path.getsize(filesrc)) / 1024
            ogfilesize = round(ogfilesize, 2)
            ogfile = str(ogfilesize)
            return ogfile
        # display compressed file size definition/function
        def display_compressedfilesize(zipnm):
            compfilesize = (os.path.getsize(zipnm)) / 1024
            compfilesize = round(compfilesize, 2)
            compfile = str(compfilesize)
            return compfile
    ogfile = display_filesize(filenm)
    compfile = display_compressedfilesize(zipnm)
    frame_status.configure(text="Original file size is " + ogfile + "Kb" + "\n Compressed file size is "+compfile+"Kb.\n")
    button_exit.grid(row= 3, column=0,padx=50, pady=31)

# decompress_file definition/function
def decompress_file():
    # Initialize the decompression parameters
    with zipfile.ZipFile(zipnm, 'r') as zip:
        # Decompress the file name provided to a folder named "extracted"
        zip.extractall(path="extracted")

# GUI Start
window = gui.CTk()
log_font = gui.CTkFont(family="Terminal", size=10)
window.geometry("495x320")
window.title(prog_nm+"-("+prog_ver+")")

def compress():
        header_compress = gui.CTkLabel(master=frame_Log, text="Correct")
        header_compress.grid(row=1, column = 0)

def option(value):
    print("segmented button clicked:", value)

def command_function(value):
        if value == "  Compression level   ":
          Compression_lvl()
        elif value == "  Help  ":
          help()

def Compression_lvl():
    style = ttk.Style()
    style.theme_use("alt")
    compression_level_window = gui_legacy.Toplevel(master=window)
    compression_level_window.configure(bg = '#1a1a1a')
    compression_level_window.geometry("400x250+200+200")
    compression_level_window.transient(master=window)
    compression_level_window.grab_set()
    compression_level_window.title("Compression Level")
    # create a label
    label = gui_legacy.Label(master=compression_level_window, text="Enter the compression level (1-9):")
    label.grid(row=0, column=0, padx=20, pady=20)
    # create an entry widget
    entry = gui_legacy.Entry(master=compression_level_window)
    entry.grid(row=1, column=0, padx=0, pady=0)
    # create a submit button
    submit_button = gui_legacy.Button(master=compression_level_window, text="Submit", command=lambda: submit_compression_level(entry.get()))
    submit_button.grid(row=2, column=0, padx=15, pady=15)
    # add a close button
    close_button = gui_legacy.Button(master=compression_level_window, text="Close", command=compression_level_window.destroy)
    close_button.grid(row=3, column=0, padx=15, pady=15)
    compression_level_window.columnconfigure(0, weight=1)

def submit_compression_level(level):
    level = int(level)
    if level < 1 or level > 9:
        messagebox.showerror("Error", "Invalid compression level")
    else:
        global levels
        levels = level
        return levels

def help():
    style = ttk.Style()
    style.theme_use("alt")
    with open('README.md','r') as f:
        help = f.read()
    compression_level_window = gui.CTkToplevel(window)
    compression_level_window.configure(bg = '#1a1a1a')
    compression_level_window.geometry("400x250+200+200")
    compression_level_window.transient(master=window)
    compression_level_window.grab_set()
    compression_level_window.title("Help")
    help_label = gui.CTkLabel(compression_level_window, text=" " + help)
    help_label.grid(row=0, column=0, padx=25, pady=31)

#side bar button
frame = gui.CTkFrame(master=window, width=160, corner_radius=0)
frame.grid(row=1, column = 0,padx=20, pady=10)

header = gui.CTkLabel(master=frame, text=prog_nm+"-("+prog_ver+")")
header.grid(row=1, column = 0, padx=20, pady=10)

button_select = gui.CTkButton(master = frame, text="Select File", command = file_browser)
button_select.grid(row=3, column=0, padx=25, pady=10)
button_compress = gui.CTkButton(master = frame, text="Compress File", command = lambda: compress_file(filesrc))
button_compress.grid(row=4, column=0, padx=25, pady=10)
button_extract = gui.CTkButton(master = frame, text="Extract ZIP", command = decompress_file)
button_extract.grid(row=5, column=0,padx=25, pady =10)
button_explore = gui.CTkButton(master = frame, text="Explore File", command = compress)
button_explore.grid(row=6, column=0, padx=25, pady=10)

#side bar log
frame_Log = gui.CTkFrame(master=window,corner_radius=0)
frame_Log.grid(row=1, column = 1,padx=0, pady=0)

frame_Log = gui.CTkLabel(master=frame_Log, text="Information")
frame_Log.grid(row=1, column = 0, padx=0, pady=20)
frame_filestatus = gui.CTkLabel(master=frame_Log, text = "No file selected.") 
frame_filestatus.grid(row=1, column=0)
frame_status = gui.CTkLabel(master=frame_Log, font=log_font, text = "No action selected.\n\n\n\n") 
frame_status.grid(row=2, column=0)
button_exit= gui.CTkButton(master=frame_Log, text = "Exit", command=exit)
button_exit.grid(row= 3, column=0,padx=50, pady=25)

button_option = gui.CTkSegmentedButton(master=window,values=["  Compression level   ","  Help  "],command=command_function)
button_option.grid(row=0, column = 0,padx=0, pady=10)

window.resizable(False, False)
window.mainloop()
