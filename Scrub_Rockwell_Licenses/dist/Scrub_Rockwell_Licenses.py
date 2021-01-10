############################################################################################
# Program/Script Title: scrub_rockwell_licenses.py
#
# Program/Script Version: 1.1
#
# Program/Script Purpose: The purpose of this script is to delete all .rnl files
#                        To repair a corrupted Rockwell Software Installation
#                        or to refresh a 7-day, fully featured trial until a
#                        license can be checked out.
#
# Program/Script Author: Alex Holburn https://www.alexholburn.com
#
# License: MIT License. Copyright 2021, Alex Holburn https://www.alexholburn.com
#
############################################################################################

# -----------------------------------BEGIN LIBRARY IMPORTS---------------------------------

from platform import system
import os
import shutil
import tkinter as main
from PIL import ImageTk, Image
import webbrowser

# -----------------------------------END LIBRARY IMPORTS-----------------------------------

# -----------------------------------BEGIN VARIABLE DECLARATIONS---------------------------

operating_system = system()
folderPath = 'C:/ProgramData/Rockwell Automation/FactoryTalk Activation'
folder_path_exists = os.path.exists(folderPath)
dirName = os.path.dirname(__file__)  # Current directory
fileName = os.path.join(dirName, r'resources\icon.ico')
archivePath = os.path.join(dirName, r'Scrubbed_RNL_Files')  # Archive path for scrubbed rnl files
icoImage = os.path.join(dirName, r'resources\icon.ico')
logoImage = os.path.join(dirName, r'resources\AlexHolburnLogo.png')  # logo image for shameless self promotion


# -----------------------------------END VARIABLE DECLARATIONS-----------------------------

# -----------------------------------BEGIN FUNCTION DEFINITIONS----------------------------

def static_description_text():  # Function to paint static description text.
    description1 = main.Label(root, text='Rockwell License Scrubber Version 1.1', fg='black', font=('Segoe', 12))
    canvas1.create_window(275, 25, window=description1)

    description2 = main.Label(root,
                              text='This utility is used to either re-enable a '
                                   '7-day trial period for Rockwell Automation',
                              fg='black', font=('Segoe', 8))
    canvas1.create_window(275, 50, window=description2)

    description3 = main.Label(root, text='Software or repair issues outlined in Rockwell KB 897947.', fg='black',
                              font=('Segoe', 8))
    canvas1.create_window(220, 66, window=description3)

    description4 = main.Label(root, text='This tool is not intended to bootleg software and/or violate copyrights.',
                              fg='black', font=('Segoe', 8, 'bold'))
    canvas1.create_window(275, 115, window=description4)


def static_status_text():  # Function to paint static status text.
    status1 = main.Label(root, text='Program Status:', fg='black', bg='White', font=('Segoe', 8,))
    canvas1.create_window(52, 186, window=status1)

    status2 = main.Label(root, text='Waiting for user input.', fg='black', bg='White', font=('Segoe', 8,))
    canvas1.create_window(67, 210, window=status2)


def generate_buttons():
    scrub_rockwell_licenses = main.Button(text='Scrub Rockwell License Files', command=scrub_rnl, )
    canvas1.create_window(275, 150, window=scrub_rockwell_licenses)


def os_type_check():  # Function to check OS Type and update status text.
    if operating_system == "Windows":  # Check if OS is Windows. 1=Status Pass 0 = Status Fail
        os_status_ok = 1
    else:
        os_status_ok = 0

    if os_status_ok == 1:  # If OS is Windows, proceed and print status message. If OS isn't Windows,
        # abort and print status message.
        status3 = main.Label(root, text='Operating System Check Status: OK (Windows).', fg='black', bg='White',
                             font=('Segoe', 8,))
        canvas1.create_window(131, 226, window=status3)
    else:
        status3 = main.Label(root, text='Operating System Check Status: FAIL (Not Windows).', fg='black', bg='White',
                             font=('Segoe', 8,))
        canvas1.create_window(144, 226, window=status3)


def file_path_check():  # Function to check if file path exists and update status text.
    if folder_path_exists is True:  # Check if OS is Windows.
        path_status_ok = 1
    else:
        path_status_ok = 0

    if path_status_ok == 1:  # If OS is Windows, proceed and print status message. If OS isn't Windows,
        # abort and print status message.
        status5 = main.Label(root,
                             text='Directory Existence Check Status: OK '
                                  '(C:/ProgramData/Rockwell Automation/FactoryTalk Activation)',
                             fg='black', bg='White', font=('Segoe', 8,))
        canvas1.create_window(256, 243, window=status5)
    else:
        status5 = main.Label(root,
                             text='Directory Existence Check Status: FAIL '
                                  '(C:/ProgramData/Rockwell Automation/FactoryTalk Activation)',
                             fg='black', bg='White', font=('Segoe', 8,))
        canvas1.create_window(258, 243, window=status5)


def move_rnl_files(old_directory, new_directory):  # Function to move rnl file directory to new location.
    shutil.move(old_directory, new_directory)


def scrub_rnl():  # scrub_rnl function. This guy does the heavy lifting for deleting RNL Files.
    os_type_check()
    if operating_system == "Windows":  # If OS is Windows, check if directory exists.
        file_path_check()

        if folder_path_exists is True:  # If Directory Exists, un-hide it and scrub files.
            move_rnl_files(folderPath, archivePath)

            if os.path.exists(
                    folderPath) is False:  # Check if License Folder was scrubbed. If folder scrubbed, Process Complete
                status6 = main.Label(root,
                                     text='Rockwell Licenses Scrubbed Status: OK '
                                          '(C:/ProgramData/Rockwell Automation/FactoryTalk Activation)',
                                     fg='black', bg='White', font=('Segoe', 8,))
                canvas1.create_window(262, 259, window=status6)

                status4 = main.Label(root, text='Process Complete.', fg='black', bg='White', font=('Segoe', 8,))
                canvas1.create_window(60, 276, window=status4)
            else:
                status7 = main.Label(root,
                                     text='Rockwell Licenses Scrubbed Status: FAIL '
                                          '(C:/ProgramData/Rockwell Automation/FactoryTalk Activation)',
                                     fg='black', bg='White', font=('Segoe', 8,))
                canvas1.create_window(265, 259, window=status7)

                status4 = main.Label(root, text='Process Aborted.', fg='black', bg='White', font=('Segoe', 8,))
                canvas1.create_window(56, 276, window=status4)

        else:
            status4 = main.Label(root, text='Process Aborted.', fg='black', bg='White', font=('Segoe', 8,))
            canvas1.create_window(56, 260, window=status4)

    else:
        status4 = main.Label(root, text='Process Aborted.', fg='black', bg='White', font=('Segoe', 8,))
        canvas1.create_window(56, 242, window=status4)


def callback(url):  # callback function. This guy lets us use URLs in an application.
    webbrowser.open_new(url)


# -----------------------------------END FUNCTION DEFINITIONS------------------------------

root = main.Tk()

# Set The Icon
root.iconbitmap(icoImage)

# Paint the canvas
canvas1 = main.Canvas(root, width=550, height=400)
canvas1.winfo_toplevel().title("Rockwell License Scrubber Version 1.1")
canvas1.pack()

# Create Status Box
canvas1.create_rectangle(10, 175, 540, 300, fill="white")

# Paint Static Description Text
static_description_text()

# Generate Buttons
generate_buttons()

# Paint Static Status Messages
static_status_text()

# Shameless Self Marketing

loadLogo = ImageTk.PhotoImage(Image.open(logoImage))
canvas1.create_image(250, 360, image=loadLogo)

link1 = main.Label(root, text="https://alexholburn.com/", fg="blue", font=('Segoe', 8, 'underline'), cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://alexholburn.com/"))

# Loop so the window appears
root.mainloop()
