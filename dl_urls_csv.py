from execute_js import execute_js

url = "http://www.images.google.com"

mtns = ["Monte Rosa", "Matterhorn"]

driver = webdriver.Chrome()

[execute_js(driver, url, mtn) for mtn in mtns]

driver.quit()