from image_downloader import ImageDownloader
import os

saved_path = '/Users/zahir/TEST/downloaded_pic'
full_uris = [
	"https://kissasian.sh/?__cf_chl_jschl_tk__=bc53fc65dc7145a68e0d694f15eef82c855d28ca-1598777077-0-AUoohWdR5whJXfJSyQkJAL-uPNPtDGeHVT7P6X7_tUHWAdTuIEWRwkL6lR_frkWTXMVd2taWIk0occy6QrKVSMRkLMRU10d3dhFc3rKUjGihIRnWVMJxpeO89y8g9_QQm5MPxMnoc5U7XaQ_8v8MluT-DHGyNihOfMUVNosrYD5_8fu62LVU00OBKMOW42NVthE4IqfdZZ5qg31lifjcg2LcTXEGXZc5NovsRgqXjm7-tTVq6jSSEdmoJ590ZoSBvFwC5gKjInos4JcDbw6UKOg",
	"https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup",
]

c = 0
onerror = False
for full_uri in full_uris:
	mkdir = saved_path + "/pic_" + str(c)
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











