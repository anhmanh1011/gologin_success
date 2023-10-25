import time
from sys import platform
from selenium import webdriver
from gologin import GoLogin
from gologin import getRandomPort
from selenium.webdriver.chrome.service import Service

gl = GoLogin({
	"token": "yU0token",
	"profile_id": "test_profile"
	})

debugger_address = gl.start()
service = Service(executable_path=r"../chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://www.python.org")

time.sleep(30)
driver.quit()
time.sleep(10)
gl.stop()
