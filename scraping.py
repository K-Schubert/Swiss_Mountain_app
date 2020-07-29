import urllib.request
import pandas as pd
from bs4 import BeautifulSoup


def scrap_mountains(n_mtns):

	url = "https://en.wikipedia.org/wiki/List_of_mountains_of_Switzerland"
	page = urllib.request.urlopen(url)

	# parse the HTML from our URL into the BeautifulSoup parse tree format
	soup = BeautifulSoup(page, "lxml")

	table = soup.find_all('table', class_='wikitable sortable')

	data_frame = pd.read_html(str(table[2]))[0]
	list_of_mountains = data_frame['Mountain'].to_list()

	if n_mtns > len(list_of_mountains):
		n_mtns = len(list_of_mountains)

	return list_of_mountains[:n_mtns]