############################################################################################
#Program/Script Title: ScrubRockwellLicenses.py
#
#Program/Script Version: 1.0
#
#Program/Script Purpose: The purpose of this script is to delete all .rnl files
#                        To repair a corrupted Rockwell Software Installation 
#                        or to refresh a 7-day, fully featured trial until a 
#                        license can be checked out. 
#
#Program/Script Author: Alex Holburn https://www.alexholburn.com 
#
#License: MIT License. Copyright 2020, Alex Holburn https://www.alexholburn.com
#
############################################################################################

#-----------------------------------BEGIN LIBRARY IMPORTS---------------------------------

import platform
from platform import system
import os, sys
import shutil
import tkinter as main 
from PIL import ImageTk, Image
import webbrowser

#-----------------------------------END LIBRARY IMPORTS-----------------------------------

#-----------------------------------BEGIN VARIABLE DECLARATIONS---------------------------

operatingSystem = system()
folderPath = 'C:/ProgramData/Rockwell Automation/FactoryTalk Activation'
folderPathExists=os.path.exists(folderPath)
dirName = os.path.dirname(__file__) #Current directory
fileName = os.path.join(dirName,'resources\icon.ico')
archivePath = os.path.join(dirName,'Scrubbed_RNL_Files') #Archive path for scrubbed rnl files
icoImage = os.path.join(dirName,'resources\icon.ico')
logoImage = os.path.join(dirName,'resources\AlexHolburnLogo.png') #logo image for shameless self promotion

#-----------------------------------END VARIABLE DECLARATIONS-----------------------------

#-----------------------------------BEGIN FUNCTION DEFINITIONS----------------------------

def staticDescriptionText (): # Function to paint static description text.
	Description1 = main.Label(root, text= 'Rockwell License Scrubber Version 1.0', fg='black', font=('Segoe', 12))
	canvas1.create_window(275, 25, window=Description1)

	Description2 = main.Label(root, text= 'This utility is used to either re-enable a 7-day trial period for Rockwell Automation', fg='black', font=('Segoe', 8))
	canvas1.create_window(275, 50, window=Description2)

	Description3 = main.Label(root, text= 'Software or repair issues outined in Rockwell KB 897947.', fg='black', font=('Segoe', 8))
	canvas1.create_window(220, 66, window=Description3)

	Description4 = main.Label(root, text= 'This tool is not intended to bootleg software and/or violate copyrights.', fg='black', font=('Segoe', 8, 'bold'))
	canvas1.create_window(275, 115, window=Description4)
	
def staticStatusText (): #Function to paint static status text.
	Status1 = main.Label(root, text= 'Program Status:', fg='black', bg='White', font=('Segoe', 8,))
	canvas1.create_window(52, 186, window=Status1)

	Status2 = main.Label(root, text= 'Waiting for user input.', fg='black', bg='White', font=('Segoe', 8,))
	canvas1.create_window(67, 210, window=Status2)

def generateButtons ():
	scrubRockwellLicenses = main.Button(text='Scrub Rockwell License Files',command=scrubRNL,)
	canvas1.create_window(275, 150, window=scrubRockwellLicenses)

def osTypeCheck (): # Function to check OS Type and update status text. 
	if operatingSystem == "Windows": # Check if OS is Windows. 1=Status Pass 0 = Status Fail
		osStatusOK = 1
	else: 
		osStatusOK = 0
		
	if osStatusOK == 1: #If OS is Windows, proceed and print status message. If OS isn't Windows, abort and print status message.
		Status3 = main.Label(root, text= 'Operating System Check Status: OK (Windows).', fg='black', bg='White', font=('Segoe', 8,))
		canvas1.create_window(131, 226, window=Status3)
	else:
		Status3 = main.Label(root, text= 'Operating System Check Status: FAIL (Not Windows).', fg='black', bg='White', font=('Segoe', 8,))
		canvas1.create_window(144, 226, window=Status3)

def filePathCheck (): #Function to check if file path exists and update status text.
	if folderPathExists == True: # Check if OS is Windows.
		pathStatusOK = 1
	else: 
		pathStatusOK = 0

	if pathStatusOK == 1: #If OS is Windows, proceed and print status message. If OS isn't Windows, abort and print status message.
		Status5 = main.Label(root, text= 'Directory Existence Check Status: OK (C:/ProgramData/Rockwell Automation/FactoryTalk Activation)', fg='black', bg='White', font=('Segoe', 8,))
		canvas1.create_window(256, 243, window=Status5)
	else:
		Status5 = main.Label(root, text= 'Directory Existence Check Status: FAIL (C:/ProgramData/Rockwell Automation/FactoryTalk Activation)', fg='black', bg='White', font=('Segoe', 8,))
		canvas1.create_window(258, 243, window=Status5)
		
def moveRNLFiles(oldDirectory,newDirectory): # Function to move rnl file directory to new location. 
	shutil.move(oldDirectory, newDirectory)
		
def scrubRNL (): #ScrubRNL function. This guy does the heavy lifting for deleting RNL Files.
	osTypeCheck ()
	if operatingSystem == "Windows": #If OS is Windows, check if directory exists.
		filePathCheck ()
		
		if folderPathExists == True: # If Directory Exists, unhide it and scrub files.
			moveRNLFiles(folderPath,archivePath)
			
			if os.path.exists(folderPath) == False: #Check if License Folder was scrubbed. If folder scrubbed, Process Complete
				Status6 = main.Label(root, text= 'Rockwell Licenses Scrubbed Status: OK (C:/ProgramData/Rockwell Automation/FactoryTalk Activation)', fg='black', bg='White', font=('Segoe', 8,))
				canvas1.create_window(262, 259, window=Status6)
				
				Status4 = main.Label(root, text= 'Process Complete.', fg='black', bg='White', font=('Segoe', 8,))
				canvas1.create_window(60, 276, window=Status4)
			else:
				Status7 = main.Label(root, text= 'Rockwell Licenses Scrubbed Status: FAIL (C:/ProgramData/Rockwell Automation/FactoryTalk Activation)', fg='black', bg='White', font=('Segoe', 8,))
				canvas1.create_window(265, 259, window=Status7)
				
				Status4 = main.Label(root, text= 'Process Aborted.', fg='black', bg='White', font=('Segoe', 8,))
				canvas1.create_window(56, 276, window=Status4)
		
		else:
			Status4 = main.Label(root, text= 'Process Aborted.', fg='black', bg='White', font=('Segoe', 8,))
			canvas1.create_window(56, 260, window=Status4)
	
	else:
		Status4 = main.Label(root, text= 'Process Aborted.', fg='black', bg='White', font=('Segoe', 8,))
		canvas1.create_window(56, 242, window=Status4)

def callback(url): #callback function. This guy lets us use URLs in an application.
	webbrowser.open_new(url)
	
#-----------------------------------END FUNCTION DEFINITIONS------------------------------

root= main.Tk()

#Set The Icon
root.iconbitmap(icoImage)

#Paint the canvase
canvas1 = main.Canvas(root, width = 550, height = 400)
canvas1.winfo_toplevel().title("Rockwell License Scrubber Version 1.0")
canvas1.pack()

#Create Status Box
canvas1.create_rectangle(10, 175, 540, 300, fill="white")

#Paint Static Description Text
staticDescriptionText () 

#Generate Buttons
generateButtons () 

#Paint Static Status Messages
staticStatusText ()

#Shameless Self Marketing

loadLogo = ImageTk.PhotoImage(Image.open(logoImage))
canvas1.create_image(250,360, image=loadLogo) 

link1 = main.Label(root, text="https://alexholburn.com/", fg="blue", font=('Segoe', 8, 'underline'), cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("https://alexholburn.com/"))

#Loop so the window appears
root.mainloop()
