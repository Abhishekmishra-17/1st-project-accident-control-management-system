import cv2
import os
from urllib.request import urlopen
import numpy as np
def extractFrames(pathOut):
    #os.mkdir(pathOut)
    url="http://192.168.43.1:8080/shot.jpg"
    count = 0
    while (True):
        #ret, frame=cap.read()
        imgResp=urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        frame=cv2.imdecode(imgNp,-1)
            
        #print('Read %d frame: ' % count, ret)
        cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
        count += 1
    # When everything done, release the capture
        cv2.imshow("hello",frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
if __name__=="__main__":
      extractFrames('frame')
      
      
