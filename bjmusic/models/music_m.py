import bjmusic.controllers.main_c
from bjmusic.models.album_m import Album 
from bjmusic import MUSICS_FILE
import datetime
import random
from time import sleep

class Music(Album):
	
	def set_id(self, _id):
		self.id = _id
	def get_id(self):
		return self.id

	def set_album(self, _album):
		self.album = _album
	def get_album(self):
		return self.album	

	def set_albumN(self, _albumN):
		self.albumN = _albumN
	def get_albumN(self):
		return self.albumN

	def set_artista(self, _artista):
		self.artista = _artista
	def get_artista(self):
		return self.artista	

	def set_titulo(self, _titulo):
		self.titulo = _titulo
	def get_titulo(self):
		return self.titulo

	def set_duracao(self, _duracao):
		self.duracao = _duracao
	def get_duracao(self):
		return self.duracao

	def set_favorita(self, _favorita):
		self.favorita = _favorita
	def get_favorita(self):
		return self.favorita


	## Escreve no arquivo uma música
	def saveMusic(self):
		try:
			with open(MUSICS_FILE, "a") as MUSICS:
				MUSICS.write(str(self.get_id()) + "\n" + str(self.get_album()) + "\n" + self.get_albumN() + "\n" + self.get_artista() + "\n" + self.get_titulo() + "\n" + str(self.get_duracao()) + "\n" + self.get_favorita() + "\n\n")
				return True
		except BaseException as e:
			bjmusic.controllers.main_c.addToLog(e)
			return False

	## Conta quantas músicas existem com base no número de linhas
	def countMusics(self):
		i=0
		with open(MUSICS_FILE, "r") as MUSICS:
			for i, l in enumerate(MUSICS):
				pass
			return int((i+1)/8)

	## Retorna um dicionario com as músicas de um album dado o ID deste album
	def searchMusicsByAlbum(self, _id):
		with open(MUSICS_FILE, "r") as MUSICS:
			l = MUSICS.readlines()
			i = 0
			musics = {}

			## Passa por todas as músicas no arquivo comparando a linha que contem o id do album com o 
			## id que recebeu
			while i in range(len(l)):
				if (i-1) % 8 == 0:
					if l[i].strip("\n") == str(_id):
						music_info = [l[i+3].strip("\n"), l[i+4].strip("\n"), l[i+5].strip("\n")]
						musics[l[i-(i%8)].strip("\n")] = music_info
						i = (i-(i%8)+8)
				i+=1

			return musics

	def searchMusic(self, keyword):
		with open(MUSICS_FILE, "r") as MUSICS:
			l = MUSICS.readlines()
			i = 0
			result = {}
			
			## Procura nas linhas do nome da banda, nome do album e titulo da musica se existe alguma 
			## correspondencia em alguma substring do arquivo com o que foi digitado 
			while i in range(len(l)):
				if not l[i] == "0":# and i%8 ==0:
					if not i%8 == 0:
						if not l[i].casefold().find(keyword.casefold().strip("\n")) == -1:
							music_info = [l[i-(i%8)+3], l[i-(i%8)+2], l[i-(i%8) +4]]
							result[l[i-(i%8)]] = music_info
							i = (i-(i%8)+8)

				i+=1
			return result

	def createPlaylist(self):
		with open(MUSICS_FILE, "r") as MUSICS:
			playlist = []
			tempo = datetime.timedelta()
			musics = []
			l = MUSICS.readlines()
			i = 0

			## Pega todas as músicas cadastradas, com título, album, duração e se é ou não uma favorita
			## sendo a key do dicionário
			while i in range(len(l)):
				if i%8 == 0:
					music_info = [l[i+2].strip("\n"), l[i+3].strip("\n"), l[i+4].strip("\n"), l[i+5].strip("\n"), l[i+6].strip("\n")]
					musics.append(music_info)
					i+=8
			i=0
			## Embaralha a lista de músicas
			random.shuffle(musics)

			## Enche mais ou menos metade da playlist com músicas favoritadas
			for i in range(len(musics)):
				if musics[i][4] == "s":
					if not str(tempo) > '0:29:00':
						t = datetime.datetime.strptime(musics[i][3], "%M:%S")
						tempo += datetime.timedelta(minutes=t.minute, seconds=t.second)
						playlist.append(musics[i])

			## Enche o resto da playlist com musicas não favoritadas
			for i in range(len(musics)):
				if musics[i][4] == "n":
					if not str(tempo) > '0:59:00':
						t = datetime.datetime.strptime(musics[i][3], "%M:%S")
						tempo += datetime.timedelta(minutes=t.minute, seconds=t.second)
						playlist.append(musics[i])
			## Embaralha a playlist
			random.shuffle(playlist)
			
			playlist.append(str(tempo))
			return playlist


