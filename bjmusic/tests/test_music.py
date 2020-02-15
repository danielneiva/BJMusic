import bjmusic.controllers.music_c
import bjmusic.models.music_m
import bjmusic.views.music_v
import unittest

class TestMusics(unittest.TestCase):
#	def test_searchMusicsByAlbum(self):
#		self.assertEqual(bjmusic.controllers.music_c.searchMusicsByAlbum(23), {'23': [ 'Bad', '4:07', 's']})

	def test_saveMusic(self):
		m = bjmusic.models.music_m.Music()
		m.set_id("0")
		m.set_album("album_id")
		m.set_albumN("album_name_&")
		m.set_artista("band_name")
		m.set_titulo("title")
		m.set_duracao("01:01")
		m.set_favorita("s")
		self.assertEqual(m.saveMusic(), True)

	def test_saveMusic_error(self):
		m = bjmusic.models.music_m.Music()
		self.assertEqual(m.saveMusic(), False)


	def test_searchMusicsByAlbum(self):
		m = bjmusic.models.music_m.Music()
		self.assertEqual(m.searchMusicsByAlbum('album_id'), {'0': ['title', '01:01', 's']})

	def test_searchMusicsByAlbum_error(self):
		m = bjmusic.models.music_m.Music()
		self.assertEqual(m.searchMusicsByAlbum("!$H!)@*U$)(U)ASU$!)@AS"), {})
		
	def test_searchMusic(self):
		m = bjmusic.models.music_m.Music()
		self.assertEqual(m.searchMusic('album_name'), {'0\n': ['band_name\n', 'album_name_&\n', 'title\n']})

	def test_searchMusic_error(self):
		m = bjmusic.models.music_m.Music()
		self.assertEqual(m.searchMusic('H!@HD(*H(*$H_J_AJD(5JEQ(J14D'), {})