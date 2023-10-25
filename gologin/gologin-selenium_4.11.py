import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from gologin import GoLogin

gl = GoLogin({
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTM3M2UwMGZlNzJmY2NiMmVkMDdjZTUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTM4YjcyZjBiMjRlM2QzZDg5ZmVmODkifQ.5XMmSpMWD0i2ieH5HFzIZ6aY9fkYv6Ph1xaXsXfHC18",
    "profile_id": "test_1"
})
gl.update({
    "id": "test_profile",
    "chromeExtensions": ["dknlfmjaanfblgfdfebhijalfmhmjjjo"]
})
debugger_address = gl.start()
service = Service(executable_path=r"../chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://nopecha.com/setup#key=I-YB20YNPT9DUE")
time.sleep(2)

driver.get("https://github.com/join")

time.sleep(30)
driver.quit()
time.sleep(10)
gl.stop()
