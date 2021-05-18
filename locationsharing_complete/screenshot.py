author="__Created by Abhishek Mishra__"
Note="""This project is only for accessing the GPS location of your android phone and sending the whatsapp messages with that location.
But you can also send the SMS and call with particular respect. For that you can follow the twilio documentation. """
print(author,end="\n")
print(Note)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client
import webbrowser
import requests
from PIL import Image
from pytesseract import pytesseract

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)# use firfox,phantomjs as per requirements

URL = 'http://192.168.43.1:8080/sensors.html'#url must be valid and live

driver.get(URL)
time.sleep(4)# take some time to open url
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot1.png')

driver.quit()
# Defining paths to tesseract.exe 
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #download pytesseract and then give the path 
image_path = r"web_screenshot1.png" #path of image
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract 
# executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
# Passing the image object to 
# image_to_string() function
# This function will
# extract the text from the image
text = pytesseract.image_to_string(img)
print(text)
str1=[]
akmstr=[]
if("Get location" in text[:-1]):
    akm=text.index("Get location")
    for i in (text[(akm):]):
        if(i.isdigit() or i=="."):
            str1.append(i)
for i in range(len(str1)):
    if(str1[i]=="."):
        akmstr.append(i)
print(akmstr)
url1=str(str1[akmstr[0]-2])+str(str1[akmstr[0]-1])+'.'+str("".join(str1[(akmstr[0]+1):(akmstr[0]+6)]))
url2=str(str1[akmstr[1]-2])+str(str1[akmstr[1]-1])+'.'+str("".join(str1[(akmstr[1]+1):(akmstr[1]+6)]))
url=(f"https://www.google.com/maps/search/?api=1&query={url1},{url2}")
print(url)
account_sid = '#' #your twilio accound Id (not userid)
auth_token = '#' #your twilio account token(not password)
client = Client(account_sid, auth_token) 
message = client.messages.create( 
                              from_='whatsapp:#',  # your twilio whatsapp number with country code
                              body=f"{url}",      
                              to='whatsapp:#' # whatsapp number on which you want to send the location
                          ) 
 
print(message.sid)
