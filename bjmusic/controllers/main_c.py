import bjmusic.controllers.music_c #as music_c
import bjmusic.controllers.album_c #as album_c
import bjmusic.views.main_v  #as main_v
import platform
import os
from time import sleep
from datetime import datetime
import sys
from bjmusic import *

def addToLog(error):
	with open(PATH_DIR + "/log.txt", "a") as f:
		f.write(str(datetime.now()) + "  -  " + str(error) + "\n\n")

def clearConsole():
	if platform.system() == "Windows":
		clear = lambda: os.system('cls')
		clear()
	elif platform.system() == "Linux":
		clear =  lambda: os.system('clear')
		clear()

def mainMenu():
	while True:
		clearConsole()
		bjmusic.views.main_v.startView()
		opt = input()
		try:
			if opt == "1":
				bjmusic.controllers.album_c.addAlbum()				
			elif opt == "2":
				bjmusic.controllers.album_c.searchAlbum()
			elif opt == "3":
				bjmusic.controllers.music_c.searchMusic()
			elif opt == "4":
				bjmusic.controllers.music_c.createPlaylist()
			elif opt == "5":
				break
				
			else:
				raise  Exception("Opção Inválida!")
		except KeyboardInterrupt:
			sys.exit(0)
		except BaseException as e:
			print(e)
			sleep(2)
			continue
	return sys.exit(0)