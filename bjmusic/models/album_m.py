from bjmusic import ALBUNS_FILE
from datetime import datetime
import bjmusic.models.music_m
import bjmusic.controllers.main_c
from time import sleep
import sys

class Album(object):
		

	def set_id(self, _id):
		self.id = _id
	def get_id(self):
		return self.id

	def set_titulo(self, _titulo):
		self.titulo = _titulo
	def get_titulo(self):
		return self.titulo

	def set_ano(self, _ano):
		self.ano = _ano
	def get_ano(self):
		return self.ano

	def set_banda(self, _banda):
		self.banda = _banda
	def get_banda(self):
		return self.banda

	def saveAlbum(self):
		try:
			with open(ALBUNS_FILE, "a") as ALBUNS:
				## Salva os dados do album no arquivo
				ALBUNS.write(str(self.get_id()) + "\n" + self.get_titulo()+ "\n"  + str(self.get_ano()) + "\n" + self.get_banda() + "\n\n")
				return True
		except BaseException as e:
			bjmusic.controllers.main_c.addToLog(e)
			return False

	##returna um dicionário no formato {id: [titulo, artista]} com todos os resultados da busca
	def searchAlbum(self, keyword): 
		with open(ALBUNS_FILE, "r") as ALBUNS:
			## Carrega os albuns salvos numa lista
			lines = ALBUNS.readlines()
			i=0
			result = {}
			while i in range(len(lines)):
				
				if not i % 5 == 0: ## Evita a linha do ID
					## Procura pela substring do usuário em cada string da lista
					if not lines[i].casefold().find(keyword.casefold().strip("\n")) == -1:
						album_info = [lines[(i-(i%5)+1)].strip("\n"), lines[(i-(i%5)+3)].strip("\n")]
						result[lines[i-(i%5)].strip("\n")] = album_info
						i = (i-(i%5)+5)

					## Printa uma linha se a posição for a ultima da lista
					if i+2 > len(lines):
						break
				i+=1
			return result


	## Conta quantas linhas tem no arquivo e divide por 5 (numero de linhas que cada album ocupa)
	def countAlbums(self):
		with open(ALBUNS_FILE, "r") as ALBUNS:
			i=0
			for i, l in enumerate(ALBUNS):
				pass
			return int((i + 1)/5)

	## Acha um album pelo ID e printa as informações dele
	def seeAlbum(self, _id):
		music = bjmusic.models.music_m.Music()
		with open(ALBUNS_FILE, "r") as ALBUNS:
			al = ALBUNS.readlines()
			i=0 
			while i in range(len(al)):
				if str(al[i].strip("\n")) ==  str(_id):
					album_info = [al[i+1].strip("\n"), al[i+2].strip("\n"), al[i+3].strip("\n"), al[i].strip("\n")]
					return album_info
				i +=1


