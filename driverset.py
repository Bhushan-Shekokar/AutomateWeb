from selenium import webdriver
#from ApplyLeave import leaveApply
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Setting:
    def set():
        service = Service(executable_path="D:\chromedriver.exe")
        # service = Service(r'C:\Users\Admin\worksjoy\venv\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("http://192.168.10.122:8012/Worksjoylite_desai_testing/#")
        driver.maximize_window()
        driver.find_element(By.ID, "email").send_keys("41002")
        # noinspection PyDeprecation
        time.sleep(3)
        driver.find_element(By.NAME, "pswd").send_keys("user@123")
        # noinspection PyDeprecation
        driver.find_element(By.CLASS_NAME, "btn-block").click()
        # Keep the browser window open permanently stop
        time.sleep(5)
        