from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def execute_js(url):
	driver = webdriver.Chrome()

	script = "urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));window.open('data:text/csv;charset=utf-8,' + escape(urls.join('" + "\\" + "n')));"

	#url = "https://www.google.com/search?tbm=isch&sxsrf=ALeKk03MLv9Cte7kUKbehP9fuVW93tFd1w%3A1595765306373&source=hp&biw=1280&bih=630&ei=OnIdX7vwFNiEk74Pz7WLoAo&q=matterhorn&oq=matterhorn&gs_lcp=CgNpbWcQA1CMAljCDWCOD2gAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwi79eqB8erqAhVYwsQBHc_aAqQQ4dUDCAc&uact=5"

	driver.get(url)

	for i in range(5):
		driver.execute_script("window.scrollTo(0, 40000);")
		time.sleep(3)

	driver.execute_script(script)

	time.sleep(5)

	driver.quit()
