from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

import time

def execute_js(driver, url, mtn):
	
	script = "urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));window.open('data:text/csv;charset=utf-8,' + escape(urls.join('" + "\\" + "n')));"

	driver.get(url)

	search = driver.find_element_by_name('q')
	#search.clear()
	search.send_keys(mtn + " mountain")
	search.send_keys(Keys.RETURN)

	for i in range(5):
		driver.execute_script("window.scrollTo(0, 40000);")
		time.sleep(1.5)

	while True:
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='YstHxe']//input[@type='button']"))).click()
			for i in range(5):
				driver.execute_script("window.scrollTo(0, 80000);")
				time.sleep(1.5)
		except ElementNotInteractableException:
			break

	driver.execute_script(script)

	time.sleep(5)
