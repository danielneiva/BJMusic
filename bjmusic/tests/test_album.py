import unittest
import bjmusic.models.album_m

class TestAlbums(unittest.TestCase):

	def test_saveAlbum(self):
		a = bjmusic.models.album_m.Album()
		a.set_id('0')
		a.set_titulo('album_name_&')
		a.set_ano('0000')
		a.set_banda('band_name')
		self.assertEqual(a.saveAlbum(), True)
		
	def test_saveAlbum_error(self):
		a = bjmusic.models.album_m.Album()
		self.assertEqual(a.saveAlbum(), False)


	def test_searchAlbum(self):
		a = bjmusic.models.album_m.Album()
		self.assertEqual(a.searchAlbum("album_name_&"), {'0':['album_name_&', 'band_name']})

	def test_searchAlbum_error(self):
		a = bjmusic.models.album_m.Album()
		self.assertEqual(a.searchAlbum("@#U!(@&#!(@*))(@#"), {})

	def test_seeAlbum(self):
		a = bjmusic.models.album_m.Album()
		self.assertEqual(a.seeAlbum('0'), ['album_name_&', '0000', 'band_name', '0'])

	def test_seeAlbum_error(self):
		a = bjmusic.models.album_m.Album()
		self.assertEqual(a.seeAlbum('asd'), None)