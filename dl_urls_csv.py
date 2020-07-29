from execute_js import execute_js
from scraping import scrap_mountains
from selenium import webdriver
import os
from paths import path

url = "http://www.images.google.com"

n_mtns = 5
mtns = scrap_mountains(n_mtns)

driver = webdriver.Chrome()

[execute_js(driver, url, mtn) for mtn in mtns]

driver.quit()

mtns = [w.replace(' ', '_') for w in mtns]

folder = mtns[0]
file = "urls_" + folder + ".csv"
path_to = "data/mountains/" + folder + "/"

if os.path.isdir(path_to):
	print("dir_exists")

os.mkdir(path_to)
os.rename(path["current"] + ".csv", path_to + file)

for i in range(1, n_mtns):
	path = path["current"] + " ({})".format(int(i)) + ".csv"
	folder = mtns[i]
	file = "urls_" + folder + ".csv"
	path_to = "data/mountains/" + folder + "/"

	os.mkdir(path_to)
	os.rename(path, path_to + file)
