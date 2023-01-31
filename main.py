#!/usr/bin/python
#
# CompressorWiz
# Group Project for a File Compression/Decompression using Python Language with TKinter GUI frontend.
#
## Members:
### Gwen Regulacion
### Angela Gallo
### John Paul Marfil
### Jedd Rasco
### Angelo Kim Hui Lim
#
## Dependencies
# Please install the following dependencies from PIP:
### customtkinter
### Pillow

# Declare important program variables
prog_nm="CompressorWiz"
prog_ver="v1.0"

# Import front-end framework
import customtkinter as gui
# Import "zipfile","datetime" and "os" module from python
import sys,zipfile,datetime,os

from tkinter.filedialog import askopenfilename
from PIL import Image

# Set GUI theme
gui.set_appearance_mode("dark")
gui.set_default_color_theme("dark-blue")
filesrc=""
filenm=""
zipnm=""
levels = 5
tmp= 5

def file_browser(event=None):
    frame_status.configure(text="No action selected.\n\n\n")
    global filesrc, filenm, zipnm
    filesrc = askopenfilename()
    filenm = filesrc.split('/')[len(filesrc.split('/'))-1]
    zipnm = os.path.splitext(filenm)[0]+".zip"
    if filenm=="":
        frame_filestatus.configure(text="No file selected.")
    else:
        filenmtruncate = (filenm[:12] + '..') if len(filenm) > 12 else filenm
        split_flex=os.path.splitext(filenm)
        file_extension=split_flex[1]
        if len(filenm)>12:
            frame_filestatus.configure(text="To compress : "+filenmtruncate+file_extension)
        else:
            frame_filestatus.configure(text="To compress : "+filenmtruncate)
        frame_filestatus.grid(pady=8)

# compress_file definition/function
def compress_file(filesrc):
    # Initialize the compression parameters
    if levels<1.0:
        with zipfile.ZipFile(zipnm, 'w') as zip:
            # Compress based on the file name provided
            zip.write(filesrc, arcname=filenm)
            # display original file size definition/function
    else:
        with zipfile.ZipFile(zipnm, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=int(levels)) as zip:  
             # Compress based on the file name provided  
             zip.write(filesrc, arcname=filenm)  
    # display original file size definition/function  
    ogfilesize = (os.path.getsize(filesrc)) / 1024  
    ogfilesize = round(ogfilesize, 2)  
    ogfile = str(ogfilesize)  
    # display compressed file size definition/function  
    compfilesize = (os.path.getsize(zipnm)) / 1024
    compfilesize = round(compfilesize, 2)
    compfile = str(compfilesize)

    frame_status.configure(text="Original file size is " + ogfile + "Kb" + "\n Compressed file size is "+compfile+"Kb.\n")
    button_exit.grid(row= 3, column=0,padx=50, pady=31)

# decompress_file definition/function
def decompress_file():
    # Initialize the decompression parameters
    with zipfile.ZipFile(zipnm, 'r') as zip:
        # Decompress the file name provided to a folder named "extracted"
        zip.extractall(path="extracted")
        frame_status.configure(text="ZIP extracted at folder ''extracted''.")

# GUI Start
window = gui.CTk()
log_font = gui.CTkFont(family="Terminal", size=10)
window.geometry("495x320")
window.title(prog_nm+"-("+prog_ver+")")

def command_function(value):
        if value == "  Compression level   ":
            Compression_lvl()
            button_option.set("None")
        elif value == "  Help   ":
            prog_help()
            button_option.set("None")

def Compression_lvl():
    compression_level_window = gui.CTkToplevel(window)
    compression_level_window.configure(bg = '#1a1a1a')
    compression_level_window.title("Compression Level")
    compression_level_window.resizable(False,False) 

    def slider_val(value): 
            global tmp
            tmp=value
            level.configure(text="Current value : "+str(int(tmp)))

    def submit_compression_level():
        global tmp
        global levels
        levels = tmp
        print("levels : ",levels)
        compression_level_window.destroy()
        compression_level_window.update()

    compress_text = gui.CTkLabel(master=compression_level_window, text="Enter the compression level (0-9):")
    compress_text.grid(row=0, column=2, padx=20, pady=0)
    compress_note = gui.CTkLabel(master=compression_level_window, text="Note that value 0 means no compression. Default is 5.\n")
    compress_note.grid(row=1, column=2, padx=20, pady=0)
    level=gui.CTkLabel(master=compression_level_window, text="Current Value : 5")
    level.grid(row=2, column=2, padx=20, pady=0)
    compress_slider = gui.CTkSlider(compression_level_window, from_=0, to=9, number_of_steps=9,command=slider_val)
    compress_slider.grid(row=4, column=2, padx=20, pady=0, sticky="ew")
    compress_button = gui.CTkButton(compression_level_window, text="Submit", command=submit_compression_level)
    compress_button.grid(row=7, column=2,padx=10, pady =10)

def prog_help():
    with open('res/help.txt','r') as f:
        help = f.read()
    help_window = gui.CTkToplevel(window)
    help_window.configure(bg = '#1a1a1a')
    help_window.title("Help")
    help_window.resizable(False,False)
    help_label = gui.CTkLabel(help_window, text=" " + help)
    help_label.grid(row=0, column=0, padx=25, pady=31)

def explore(zip_name):
    explore_window = gui.CTkToplevel(window)
    explore_window.configure(bg = '#1a1a1a')
    explore_window.title("Explore")
    explore_window.resizable(False,False)
    with open ("fileinfo",'a') as sys.stdout:
        with zipfile.ZipFile(zip_name, mode="r") as archive:
            for info in archive.infolist():
                print(f"\nFile inside: {info.filename}")
                print(f"Modified: {datetime.datetime(*info.date_time)}")
                print(f"Normal size: {info.file_size} bytes")
                print(f"Compressed size: {info.compress_size} bytes")
    with open("fileinfo",'r') as fileinfotxt:
        fileinfo=fileinfotxt.read()
    explore_text=gui.CTkLabel(explore_window, text=" "+fileinfo)
    os.remove("fileinfo")
    explore_text.grid(row=0, column=2, padx=20, pady=0)

#side bar buttons
frame = gui.CTkFrame(master=window, height=250, width=191, corner_radius=0)
frame.grid(row=1, column = 0,padx=20, pady=10)
frame.grid_propagate(False)
header = gui.CTkLabel(master=frame, text=prog_nm+"-("+prog_ver+")")
header.grid(row=1, column = 0, padx=20, pady=10)
button_select = gui.CTkButton(master = frame, text="Select File", command = file_browser)
button_select.grid(row=3, column=0, padx=25, pady=10)
button_compress = gui.CTkButton(master = frame, text="Compress File", command = lambda: compress_file(filesrc))
button_compress.grid(row=4, column=0, padx=25, pady=10)
button_extract = gui.CTkButton(master = frame, text="Extract ZIP", command = decompress_file)
button_extract.grid(row=5, column=0,padx=25, pady =10)
button_explore = gui.CTkButton(master = frame, text="Explore File", command = lambda: explore(zipnm))
button_explore.grid(row=6, column=0, padx=25, pady=10)

#side bar logs
frame_Log = gui.CTkFrame(master=window, height=250, width=245, corner_radius=0)
frame_Log.grid(row=1, column = 1,padx=0, pady=0)
frame_Log.grid_propagate(False)
frame_Log = gui.CTkLabel(master=frame_Log, text="Information")
frame_Log.grid(row=1, column = 0, padx=0, pady=20)
frame_filestatus = gui.CTkLabel(master=frame_Log, text = "No file selected.") 
frame_filestatus.grid(row=1, column=0)
frame_status = gui.CTkLabel(master=frame_Log, font=log_font, text = "No action selected.\n\n\n\n") 
frame_status.grid(row=2, column=0)
button_exit= gui.CTkButton(master=frame_Log, text = "Exit", command=exit)
button_exit.grid(row= 3, column=0,padx=50, pady=25)

# menu
button_option = gui.CTkSegmentedButton(master=window,values=["  Compression level   ","  Help   "],command=command_function)
button_option.grid(row=0, column = 0,padx=0, pady=10)

# logo
tuplogo = gui.CTkImage(light_image=Image.open("res/logo.png"), dark_image=Image.open("res/logo.png"),size=(20, 20))
logo = gui.CTkButton(master = window, image=tuplogo, text="TUP - Manila Campus", fg_color="transparent", hover=False)
logo.grid(row=0, column=1, padx=0, pady=10)
window.resizable(False, False)
window.mainloop()
