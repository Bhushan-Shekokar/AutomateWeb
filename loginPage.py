from selenium import webdriver
import driverset
import ApplyLeave
from driverset import Setting
from ApplyLeave import leaveApply
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
import time

class login:
    driverset.Setting
    s = Setting   # create object of class Setting.
    s.set()

    #service = Service(executable_path="D:\chromedriver.exe")
    # service = Service(r'C:\Users\Admin\worksjoy\venv\chromedriver.exe')
    #driver = webdriver.Chrome(service=service)
    time.sleep(2)
    # service = Service(r'C:\Users\Admin\worksjoy\venv\chromedriver.exe')
    # driver = webdriver.Chrome(service=service)
    # driver=webdriver.Chrome(executable_path=r'C:\Users\Admin\worksjoy\venv\chromedriver.exe')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #d= driverset
    #d.Setting()
    print("Setting accepted correctly")
    time.sleep(2)
ApplyLeave.leaveApply
lv = leaveApply      # create an object of the class
lv.applylv()         # call method of ApplyLeave file
print("apply leave setting done.")
time.sleep(3)
    # driver.quit()  



