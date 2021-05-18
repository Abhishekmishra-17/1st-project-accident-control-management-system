import urllib.request
import json
import location
while(1):
    URL = 'http://192.168.43.1:8080/sensors.json'
    data = urllib.request.urlopen(URL).read().decode()
    obj = json.loads(data)
    #print(obj)
    obj_data = obj['accel']['data']
    #print(obj_data)
    akm=len(obj_data)
    akm_data=obj_data[akm-1][1]
    print(akm_data[0],akm_data[1],akm_data[2])
    miv=-10#min_value minimum threshold
    mav=10#max_value maximum threshold
    if((mav<=akm_data[0] or akm_data[0]<=miv)or(mav<=akm_data[1] or akm_data[1]<=miv) or(mav<=akm_data[2] or akm_data[2]<=miv)):
        location.main()
        break
    else:
        print("Safe")
        
    
