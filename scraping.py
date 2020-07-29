import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_mountains_of_Switzerland"
page = urllib.request.urlopen(url)

from bs4 import BeautifulSoup

# parse the HTML from our URL into the BeautifulSoup parse tree format
soup = BeautifulSoup(page, "lxml")

table = soup.find_all('table', class_='wikitable sortable')

data_frame = pd.read_html(str(table[2]))[0]
list_of_mountains = data_frame['Mountain'].to_list()

#list_of_mountains = [w.replace(' ', '_') for w in list_of_mountains]

print(list_of_mountains[:10])