from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import os

class Scraper:
	def __init__(self):
		try:
			firefox_options = Options()
			firefox_options.add_argument("--headless")
			self.driver = webdriver.Firefox(options=firefox_options)
		except Exception as error:
			print(error)

	def download(self, url):
		try:
			self.driver.get(url)
			html = self.driver.page_source
		except Exception as error:
			print(error)
		return(html)

def export(html, output_file):
	try:
		f = open(output_file, "a")
		f.write(html)
		f.close()
		status = True
	except Exception as error:
		status = False
		print(error)
	return(status)

#############################################################################

path1 = "/home/user/Desktop/scraper/"
url1 = "https://www.google.com/"

os.chdir(path1)
scraper1 = Scraper()
test1 = scraper1.download(url1)
export1 = export(test1, "test1.html")

