import time
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service

path = Service("C:\\Users\sarve\\Downloads\\edgedriver_win64\\msedgedriver.exe")
print('\nLaunching Browser...')
driver = webdriver.Edge(service=path)
print('\nMaximizing Brower...')
driver.maximize_window()
print('\nRedirecting to https://www.mtribes.com...')
driver.get('https://www.mtribes.com/')
print('\nWaiting For 5 Seconds...')
time.sleep(5)
print('\nEntering Credentials & Login...')
driver.find_element("xpath", "//input[@id='signInName']").send_keys('raikar.mansi3@gmail.com')
driver.find_element("xpath", "//input[@id='password']").send_keys('Mansi8496@')
driver.find_element("xpath", "//button[@id='next']").click()
time.sleep(2)
print('\nVerifying User Logged In or Not...')
counter = 10
while counter != 0:
    exists = len(driver.find_elements("xpath", "//div[@class='css-1tclw4p']"))
    if exists > 0:
        print('\nUser Logged In Successfully...')
        break
    else:
        time.sleep(5)
        counter = counter - 1
        if counter == 0:
            print('\nUser Failed to Login...')
            sys.exit(0)
        else:
            print('\nVerifying User Login, Retry : ' + str(counter))

print('\nLogging Out User...')
driver.find_element("xpath", "//div[@class='css-1tclw4p']").click()
time.sleep(3)
driver.find_element("xpath", "//li[3]/button[1]").click()
time.sleep(5)
print('\nUser Successfully Logged Out...')
driver.close()
sys.exit(0)
