# importing the libraries
from bs4 import BeautifulSoup
import requests
import os

class ImageDownloader:

    def __init__(self, url, url_path, save_path, onerror):
	    self.url = url
	    self.url_path = url_path
	    self.save_path = save_path
	    self.list_of_images = []
	    self.onerror = onerror
	    self.getImageLinkByWeb()
	    self.downloadAll()

    def getImageLinkByWeb(self):
    	if self.onerror == False:
    		print("getting all images from: \n%s..." % self.url + self.url_path)
    		# Make a GET request to fetch the raw HTML content
    		html_content = requests.get(self.url + self.url_path).text
    		# Parse the html content
    		soup = BeautifulSoup(html_content, "html.parser")
    		for link in soup.find_all("img"):
    			self.list_of_images.append(format(link.get("src")))
    		if len(self.list_of_images) == 0:
    			os.rmdir(self.save_path)
    			print("Image not found!")
    			self.onerror = True
    		else:
    			print("Images is ready")

    def downloadAll(self):
    	if self.onerror == False:
    		print("downloading...")
    		c = 1
    		max_c = len(self.list_of_images)
    		for i in self.list_of_images:
    			if i[0] == "/":
    				print("[" + str(c) + "/" + str(max_c) + "] Downloading " + self.url + i)
    				img_from = self.url + i
    			elif i[:4] != "http":
    				print("[" + str(c) + "/" + str(max_c) + "] Downloading " + self.url + "/" + i)
    				img_from = self.url + "/" + i
    			else:
    				print("[" + str(c) + "/" + str(max_c) + "] Downloading " + i)
    				img_from = i
    			save_img = self.save_path + "/" + os.path.basename(i)
    			try:
    				r = requests.get(img_from)
    				with open(save_img, 'wb') as f:
    					f.write(r.content)
    					print("Downloaded at " + self.save_path + "/" + os.path.basename(i))
    			except:
    				print("[ERROR] An exception occurred")
    				self.onerror = True
    			c = c+1
    			if self.onerror == False:
    				print("Image from [" + self.url + self.url_path + "] is downloaded.")













