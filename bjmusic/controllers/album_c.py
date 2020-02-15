import bjmusic.models.album_m 
import bjmusic.views.album_v 

def searchAlbum():
	album = bjmusic.models.album_m.Album()
	keyword = bjmusic.views.album_v.searchAlbum()
	return bjmusic.views.album_v.searchAlbum(album.searchAlbum(keyword))

def seeAlbum():
	album = bjmusic.models.album_m.Album()
	_id = bjmusic.views.album_v.seeAlbum()
	if _id:
		return bjmusic.views.album_v.seeAlbum(album.seeAlbum(_id))

def addAlbum():
	album = bjmusic.models.album_m.Album()
	album_info = bjmusic.views.album_v.addAlbum()
	album.set_titulo(album_info[0])
	album.set_ano(album_info[1])
	album.set_banda(album_info[2])
	album.set_id(album_info[3])
	album.saveAlbum()
	bjmusic.views.album_v.addAlbum("mus")
	bjmusic.controllers.music_c.addMusic(album)
	
