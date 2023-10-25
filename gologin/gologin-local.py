import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin


gl = GoLogin({
	"token": "ayJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTM3M2UwMGZlNzJmY2NiMmVkMDdjZTUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTM4YjcyZjBiMjRlM2QzZDg5ZmVmODkifQ.5XMmSpMWD0i2ieH5HFzIZ6aY9fkYv6Ph1xaXsXfHC18",
	"profile_id": "test_profile",
	"local": True,
	"credentials_enable_service": False,
	})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.quit()
time.sleep(3)
gl.stop()
