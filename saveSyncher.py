#!/bin/python

from Tkinter import *
from tkFileDialog import askdirectory
import ConfigParser
import os.path
import getpass
configObject = ConfigParser.RawConfigParser()


def initializeCfg():
	configObject.add_section("watchedDirs")
	configObject.add_section("other")
	configObject.set("other", "repoDir", "C:\\Users\\" + getpass.getuser() + "\\Dropbox\\saveSyncher\\")



def readData():
	if os.path.isfile("saveSyncher.cfg"):
		cfg = open("saveSyncher.cfg")
	else
		cfg = open("saveSyncher.cfg")
		initializeCfg


def synchFolder():

def synchAll():

def synchOne():

def addDir():

def setRepo():
	print("NOTE: this folder must be in some sort of shared folder")
	print("(ie dropbox, git, etc.). This program does not provide")
	print("the remote storage server.")
	print("")



def mainMenu():
	print("What do you want to do?\n")
	print("[1] Sync all watched directories.")
	print("[2] Sync a specific save directory.")
	print("[3] Add a save directory to watch.")
	print("[4] Change the repository directory.")
	print("[5] Quit")
	option = input();

	if option == 1:
		synchAll()
	elif option == 2:
		synchOne()
	elif option == 3:
		addDir()
	elif option == 4:
		setRepo()
	elif option == 5:
		sys.exit(0)
	else:
		print("invalid selection.")





#main
readData()
mainMenu()