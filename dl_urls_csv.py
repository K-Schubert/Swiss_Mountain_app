
from execute_js import execute_js
from scraping import scrap_mountains
from selenium import webdriver

url = "http://www.images.google.com"

n_mtns = 1
mtns = scrap_mountains(n_mtns)

driver = webdriver.Chrome()

[execute_js(driver, url, mtn) for mtn in mtns]

driver.quit()

import os
import shutil
'''
os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
'''
from paths import path

folder = mtns[0]
file = "urls_" + folder + ".csv"
path_to = "data/mountains/" + folder + file

os.rename(path + ".csv", path_to)
shutil.move(path + ".csv", path_to)
os.replace(path + ".csv", path_to)

n_mtns = 1
for i in range(1, n_mtns):
	path = path + " ({})".format(i) + ".csv"
	folder = mtns[i]
	file = "urls_" + folder + ".csv"
	path_to = "data/mountains/" + folder + file
	os.rename(path, path_to)
	shutil.move(path, path_to)
	os.replace(path, path_to)
