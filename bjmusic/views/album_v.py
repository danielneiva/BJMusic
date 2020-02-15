import bjmusic.controllers.music_c #as music_c
import bjmusic.controllers.main_c #as main_c
import bjmusic.controllers.album_c
from time import sleep
import sys

def searchAlbum(par=""):
	while True:
		try:
			if par == "":
				inpt = input("Digite o nome do artista, o titulo do album ou o ano: \n")
				if inpt == "":
					raise Exception("Você digitou algo inválido!")
				return inpt
			else:
				sleep(0.25)
				bjmusic.controllers.main_c.clearConsole()
				print("\n\nLista de albuns: \n\n")
				for r in par:
					print("-------------------------------------------------\n" + r + "   |  " + par[r][0] + " - " + par[r][1])
				bjmusic.controllers.album_c.seeAlbum()
				break
		except KeyboardInterrupt:
			sys.exit(0)
		except Exception as e:
			print(e)
			continue	
		except:
			print("Ocorreu um erro :(\nO programa irá fechar")
			sys.exit(0)
			
def seeAlbum(par=""):
	album = bjmusic.models.album_m.Album()
	while True:		
		try:
			if par == "":
				opt = input("Digite o número do album para mais informações ou 0 para voltar: \n")
				if opt == "0":
					break
				elif not opt.isdigit():
					raise Exception("Você digitou algo errado!")
				elif int(opt) <0:
					raise Exception("Você digitou algo errado!")
				elif int(opt) > album.countAlbums():
					raise Exception("Esse album não existe!")
				else:
					return opt
					
			else:
				bjmusic.controllers.main_c.clearConsole()
				print("\nTítulo: " + par[0] + "\nAno: " + par[1] + "\nBanda: " + par[2])
				bjmusic.controllers.music_c.searchMusicsByAlbum(par[3])
				break
		except KeyboardInterrupt:
			sys.exit(0)
		except Exception as e:
			print(e)
			continue
		

			
def addAlbum(par = ""):
	while True:
		try:
			if par == "":
				album = bjmusic.models.album_m.Album()
				album_info = []
				inp = input("Qual o título do album?\n")
				album_info.append(inp)
				while True:
					try:
						inp = input("Qual o ano do album?\n")
						if not inp.isdigit():
							raise TypeError("Digite um ano!!!")
						elif int(inpt):
							album_info.append(inp)
							break
					except Exception as e:
						print (e)
						sleep(2)
					except KeyboardInterrupt:
						sys.exit(0)
				inp = input("Qual o nome da banda?\n")
				album_info.append(inp)
				album_info.append(album.countAlbums()+1)
				return album_info
			elif par == "mus":
				bjmusic.controllers.main_c.clearConsole()
				print("Adicione Músicas ao album que você salvou!")
				sleep(2)
				break
		except KeyboardInterrupt:
			sys.exit()
			break
		except BaseException as e:
			print(e)


