from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
import time
def getLocation():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(executable_path = './chromedriver.exe',options=options)
    #Edit path of chromedriver accordingly
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath    
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()
    print("The current location of emergency area is as below..\n")
    print("The latitude is",latitude,"and longitude is",longitude,"\n")
    print("Please send a help immediately....")
    return (latitude,longitude)
getLocation()
