from execute_js import execute_js
from scraping import scrap_mountains
from selenium import webdriver
import os
from paths import path

def dl_urls_csv(n_mtns):

	url = "http://www.images.google.com"

	# Get mountain names from Wikipedia
	mtns = scrap_mountains(n_mtns)

	driver = webdriver.Chrome()

	# Download photo urls for each mountain
	for mtn in mtns:
		execute_js(driver, url, mtn)

	driver.quit()

	mtns = [w.replace(' ', '_') for w in mtns]

	folder = mtns[0]
	file = "urls_" + folder + ".csv"
	path_to = "data/mountains/" + folder + "/"

	'''
	if os.path.isdir(path_to):
		print("dir_exists")
	'''

	# Create data folders and move urls
	os.mkdir(path_to)
	os.rename(path["current"] + ".csv", path_to + file)

	for i in range(1, n_mtns):
		folder = mtns[i]
		file = "urls_" + folder + ".csv"
		path_to = "data/mountains/" + folder + "/"

		os.mkdir(path_to)
		os.rename(path["current"] + " ({})".format(i) + ".csv", path_to + file)
