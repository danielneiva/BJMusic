import bjmusic.models.music_m
import bjmusic.views.music_v
import sys

def searchMusicsByAlbum(id):
	music = bjmusic.models.music_m.Music()
	result = music.searchMusicsByAlbum(id)
	return bjmusic.views.music_v.searchMusicsByAlbum(result)

def addMusic(album):
	while True:
		try:
			music = bjmusic.models.music_m.Music()
			music_info = bjmusic.views.music_v.addMusic(album)
			music.set_titulo(music_info[0])
			music.set_duracao(music_info[1][0:2] + ":" + music_info[1][2:4])
			music.set_favorita(music_info[2])
			music.set_artista(music_info[3])
			music.set_album(music_info[4])
			music.set_albumN(music_info[5])
			music.set_id(music.countMusics()+1)

			if music.saveMusic():
				try:
					print("Tem outra música para adicionar? (S/N)")
					opt = input()
					if opt.casefold() == "s":
						continue
					elif opt.casefold() == "n":
						break
					else:
						raise Exception("Opção inválida!")
				except Exception as e:
					print(e)
			else:
				raise Exception("Não foi possível salvar a música")
		except Exception as e:
			print(e)
		except KeyboardInterrupt:
			sys.exit(0)

def searchMusic():
	try:
		music = bjmusic.models.music_m.Music()
		inpt = bjmusic.views.music_v.searchMusic()
		result = music.searchMusic(inpt)
		return bjmusic.views.music_v.searchMusic(result)
	except BaseException as e:
		print(e)
		print("Para sua segurança, o programa irá fechar :(")
		sys.exit(0)
	except KeyboardInterrupt:
		sys.exit(0)

def createPlaylist():
	music = bjmusic.models.music_m.Music()
	playlist = 	music.createPlaylist()
	bjmusic.views.music_v.createPlaylist(playlist)