from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class leaveApply:
    

    def applylv():
        #service = Service(executable_path="D:\chromedriver.exe")
        # service = Service(r'C:\Users\Admin\worksjoy\venv\chromedriver.exe')
        #driver = webdriver.Chrome(service=service)
        driver.find_element(By.CSS_SELECTOR,"#sidebarnav > li:nth-child(4) > a").click()
        time.sleep(2)
       # driver.find_element(By.CSS_SELECTOR,
       #                     "body > app-root > app-layout > div.container-fluid.ng-star-inserted > div > app-attendancemenu > div > div > div > div > div > div.p-3 > div > ul > li:nth-child(2) > div").click()
       # time.sleep(2)
        # Find the drop-down element
       # driver.find_element(By.XPATH,
       #                     "/html/body/app-root/app-layout/div[2]/div/app-leaverequest/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/form/div[1]/select/option[3]").click()
        # select the desired element from dropdown listtextbox.send_keys("Apply Leave")

        # Select osel  = new Select(driver.findElement(By.xpath(By.XPATH,("//*[@id='pills-home']/div[1]/div/div[2]/div/form/div[1]/select")))
        #                      if(osel.selectByIndex)
        # se.selectByVisibility("Privilege Leave").click()
       # textbox = driver.find_element(By.CSS_SELECTOR,
       #                               "#pills-home > div:nth-child(1) > div > div:nth-child(2) > div > form > div.ng-star-inserted > div:nth-child(3) > input")
        # /html/body/app-root/app-layout/div[2]/div/app-leaverequest/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/form/div[1]/select/option[3]
        # //*[@id='pills-home']/div[1]/div/div[2]/div/form/div[1]/select
        # textbox= driver.find_element(By.CSS_SELECTOR,"#pills-home > div:nth-child(1) > div > div:nth-child(2) > div > form > div.ng-star-inserted > div:nth-child(6) > input")
        # textbox.send_keys("please Apply Leave")
       # time.sleep(4)
       # driver.find_element(By.XPATH,
       #                     "//*[@id='pills-home']/div[1]/div/div[2]/div/form/div[2]/div[8]/button[1]").click()
        # while True:
       # time.sleep(5)







