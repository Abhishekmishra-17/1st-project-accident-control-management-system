def main():
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
    driver = webdriver.Chrome(options=options)

    URL = 'http://192.168.43.1:8080/sensors.html'

    driver.get(URL)
    time.sleep(3)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
    driver.find_element_by_tag_name('body').screenshot('web_screenshot1.png')

    driver.quit()
    # Defining paths to tesseract.exe 
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"web_screenshot1.png"
      
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
    #print(text)
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
    #print(akmstr)
    url1=str(str1[akmstr[0]-2])+str(str1[akmstr[0]-1])+'.'+str("".join(str1[(akmstr[0]+1):(akmstr[0]+6)]))
    url2=str(str1[akmstr[1]-2])+str(str1[akmstr[1]-1])+'.'+str("".join(str1[(akmstr[1]+1):(akmstr[1]+6)]))
    url=(f"https://www.google.com/maps/search/?api=1&query={url1},{url2}")
    #print(url)
    account_sid = '#' 
    auth_token = '#' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                                  from_='whatsapp:+14#',  
                                  body=f"{url}",      
                                  to='whatsapp:+91#' 
                              )
    account_sid = '#'
    auth_token = '#'
    client = Client(account_sid, auth_token)
    message = client.messages \
          .create(
                     body=f"{url}",
                     from_='+1#',
                     to='+91#'
                 )
     
    #print(message.sid)
if __name__=="__main__":
    main()
