import cv2
import imutils
import pytesseract
import numpy as np
from urllib.request import urlopen
import pandas as pd
import re
lak=[]
code={"Andaman and Nicobar":"AN","Andhra Pradesh":"AP","Arunachal Pradesh":"AR","Assam":"AS","Bihar":"BR",
"Chandigarh":"CH","Dadra and Nagar Haveli":"DN","Daman and Diu":"DD","Delhi":"DL","Goa":"GA","Gujarat":"GJ",
"Haryana":"HR","Himachal Pradesh":"HP","Jammu and Kashmir":"JK","Karnataka":"KA","Kerala":"KL","Lakshadweep":"LD",
"Madhya Pradesh":"MP","Maharashtra":"MH","Manipur":"MN","Meghalaya":"ML","Mizoram":"MZ","Nagaland":"NL",
"Orissa":"OR","Pondicherry":"PY","Punjab":"PN","Rajasthan":"RJ","Sikkim":"SK","TamilNadu":"TN","Tripura":"TR",
"Uttar Pradesh":"UP","West Bengal":"WB"}

match_pattern="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$" # custom format for plate number sampling
match_pattern1="[A-Z]{2}[0-9]{2}[A-Z]{1}[0-9]{4}$"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
url="http://192.168.43.1:8080/shot.jpg"
while True:
    imgResp=urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.resize(img, (620,480) )
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
    gray = cv2.bilateralFilter(gray, 13, 15, 15)
    edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
    contours=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]
    #print(contours)
    screenCnt = None
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
    # Masking the part other than the number plate
    if screenCnt is not None:
        mask = np.zeros(gray.shape,np.uint8)
        new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
        new_image = cv2.bitwise_and(img,img,mask=mask)
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]
        cv2.imshow("result",new_image)
        text = pytesseract.image_to_string(Cropped)
        text=list(text.split(" "))
        text="".join(text)
        text=text.upper()
        text=text[:10]
        print(text,len(text))
        akm=re.match(match_pattern,text)
        akm1=re.match(match_pattern1,text)
        print(bool(akm))
        dict1=""
        if(bool(akm)or bool(akm1)):
            for (item,value) in code.items():
                print(text[:2],value)
                if(text[:2]==value):
                   dict1=[item]
            print(dict1)
            if(dict1):
                dicta=[text]
                df=pd.DataFrame([[dicta,dict1]], columns=["plate_number","state-Name"])
                df.to_csv("plate.csv")
                df_homes = pd.read_csv("plate.csv")
                df_homes1 = pd.read_csv("PlateNumber_complete.csv")
                pd.concat([ df_homes1,df_homes]).to_csv('PlateNumber_complete.csv', index=False)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
for i in lak:
    i.to_csv("PlateNumber.csv",index=1)
cv2.destroyAllWindows()
