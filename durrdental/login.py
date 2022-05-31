from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("start-maximized")
driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://vsmonitor.com/")

driver.find_element_by_id("email").send_keys("dd_test_1@outlook.com")
driver.find_element_by_id("password").send_keys("}krK,gdC6")

driver.find_element_by_id("login-button").click()

driver.find_elements_by_link_text("https://vsmonitor.com/").__init__()

#driver.find_elements_by_id("nav-user-button").pop()


time.sleep(2)
driver.close()
driver.quit()
print("Login Success")
