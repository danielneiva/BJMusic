import bjmusic.controllers.main_c
from time import sleep

def searchMusicsByAlbum(result):
	try:
		print("\n\n\n\n----------------------------\n\n")
		print("\nLista de Músicas: \n\n")
		for r in result:
			print("----------------------------")
			print("\nTítulo: " + result[r][0] + "\nDuração: " + result[r][1])
			if result[r][2].casefold() == "s":
				print("É uma favorita? SIM!!!")
			else: 
				print("É uma favorita? Não!")
		volt = input("\n\n\nDigite qualquer tecla para voltar\n")
		return result
	except KeyboardInterrupt:
		sys.exit(0)
	except BaseException as e:
		print(e)
	

def addMusic(album):
	bjmusic.controllers.main_c.clearConsole()
	while True:
		try:
			music = []
			print("\n\n Adicionar Música\n\nQual o título da música?\n")
			music.append(input())
			while True:
				try:
					inpt = input("Qual a duração da música? (mmss)\n")
					if not inpt.isdigit():
						raise Exception("Digite uma duração válida!!!")
					elif int(inpt[0:2]) >= 60 or int (inpt[2:4]) >= 60 or int(inpt[0:2]) < 0 or int (inpt[2:4]) <0:
						raise Exception("Digite uma duração válida!!!")
					else:
						music.append(inpt)
						break
				except KeyboardInterrupt:
					sys.exit(0)
				except Exception as e:
					print(e)
					sleep(1.5)
					continue

			
			while True:
				inpt = input("A música é uma das suas favoritas? (S/N)\n").casefold()
				if not inpt.casefold() == "s" and not inpt.casefold() == "n":
					raise Exception("Opção errada!")
					continue
				else:
					music.append(inpt.casefold())
					break
			music.append(album.get_banda())
			music.append(album.get_id())
			music.append(album.get_titulo())
			return music
		except KeyboardInterrupt:
			break
			sys.exit(0)
		except BaseException as e:
			print(e)
			sleep(2)
		

def searchMusic(par=""):
	while True:
		try:
			bjmusic.controllers.main_c.clearConsole()
			if par == "":
				inpt = input("\n Digite o que você quer pesquisar: \n")
				if inpt == "":
					raise Exception("Você digitou algo inválido!")
				return inpt
			else:
				for r in par:		
					print("-------------------------------------------\n" + "Título: " + par[r][2] + "Artista: " + par[r][0] + "Album: " + par[r][1])
				print("-------------------------------------------\n")
				input("Digite algo para voltar")
				break
		except KeyboardInterrupt:
			sys.exit(0)
		except Exception as e:
			print(e)
			continue

def createPlaylist(playlist):
	bjmusic.controllers.main_c.clearConsole()
	print("\n\nAproveite esta playlist novinha :) \n\n")
	i = 0
	for i in range(len(playlist)):
		print(playlist[i][2] + "  -  " + playlist[i][1] + "  -  " + playlist[i][3])
		if i+2 == len(playlist):
			print("Duração total:  " + playlist[i+1])
			i+=2
			break

	input("\n\n\nDigite algo para voltar\n")
	return True
		