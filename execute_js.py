from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException

import time

def execute_js(url, mtn):
	driver = webdriver.Chrome()

	script = "urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));window.open('data:text/csv;charset=utf-8,' + escape(urls.join('" + "\\" + "n')));"

	driver.get(url)

	search = driver.find_element_by_name('q')
	search.send_keys(mtn + " mountain")
	search.send_keys(Keys.RETURN)

	for i in range(5):
		driver.execute_script("window.scrollTo(0, 40000);")
		time.sleep(1.5)

	time.sleep(3)

	while True:
		try:
			driver.find_element_by_xpath("//div[@class='YstHxe']//input[@type='button']").click()
			time.sleep(1.5)
			for i in range(5):
				driver.execute_script("window.scrollTo(0, 80000);")
				time.sleep(1.5)
		except ElementNotInteractableException:
			break

	driver.execute_script(script)

	time.sleep(5)

	driver.quit()


url = "http://www.images.google.com"

execute_js(url, "Matterhorn")

