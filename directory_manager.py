from image_downloader import ImageDownloader
import os

class DirectoryManager:

	def __init__(self, full_uris, saved_path):
		self.full_uris = full_uris
		self.saved_path = saved_path
		self.createDir()

	def createDir(self):
		c = 0
		onerror = False
		for full_uri in self.full_uris:
			mkdir = self.saved_path + "/uri_" + str(c)
			access_rights = 0o755
			print ("Creating directory at %s " % mkdir)
			try:
				if not os.path.exists(mkdir):
					os.makedirs(mkdir, access_rights)
					print ("Successfully created the directory %s " % mkdir)
				else:
					print("Directory at %s is already exists!\n" % mkdir)
					onerror = True
			except OSError:
				print("Failed to create directory at %s\n" % mkdir)
				break
			
			url = os.path.split(full_uri)[0]
			if len(url) < 6:
				url = full_uri
				url_path = ""
			else:
				url_path = "/" + os.path.split(full_uri)[1]
			ImageDownloader(url, url_path, mkdir, onerror)
			print("")
			c += 1
		print("Done.")










