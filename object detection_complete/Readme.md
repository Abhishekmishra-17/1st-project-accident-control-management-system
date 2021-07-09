## What is Object Detection?
Object detection is a branch of computer vision which deals with the localization and the identification of an object. Object localization and identification are two different tasks that are put together to achieve this singular goal of object detection.<br>
Specifying the location of an object in an image or a video stream is called object localization and assigning the object to a specific label, class, or description is called object identification.<br>
 Some architectures that have performed tremendously well on the **<a href="https://drive.google.com/file/d/1whaHiSKfcb1Iws62Bzb-j2qeYx4WsZa-/view?usp=sharing">COCO dataset</a>**.<br>
The model architectures include:<br>
*1. CenterNet<br>
2. EfficientDet<br>
3. MobileNet<br>
4. ResNet<br>
5. R-CNN<br>
6. ExtremeNet<br>*

Here we are going to use `MobileNet` architecture. Download the architecture from <a href="https://drive.google.com/file/d/1u7Fy7sS8Xp39HKgjhjuwlbDN7s5l1wjh/view?usp=sharing">Here</a><br>
<b> MobileNet</b> is an object detector (2017) used as an efficient CNN architecture designed for mobile and embedded vision application. This architecture uses proven depth-wise separable convolutions to build lightweight deep neural networks. More information about the architecture can be found <a href="https://drive.google.com/file/d/1bxU16LQOs2MR6wCmpehwn6s_-S5dN4_B/view?usp=sharing">Here</a>.<br>
## Optimizing the model
Freezing the model means producing a singular file containing information about the graph and checkpoint variables, but saving these hyperparameters as constants within the graph structure. This eliminates additional information saved in the checkpoint files such as the gradients at each point, which are included so that the model can be reloaded and training continued from where you left off. As this is not needed when serving a model purely for inference they are discarded in freezing.
For more details checkout <a href="https://cv-tricks.com/how-to/freeze-tensorflow-models/#:~:text=Freezing%20is%20the%20process%20to,a%20serialized%20MetaGraphDef%20protocol%20buffer.">This</a>.
Download the `frozen_inference_graph.pb` freezing model from <a href="https://drive.google.com/file/d/1Z-6HOmtKEnFc-pV_GEJURFadQY2rDDba/view?usp=sharing">Here</a>.

## Working
This module is a part of Accident Control Management System. This will helpful in detection and recognition of objects. With this if any things is comes in front of vehicle then it will detect that and display the visuals. With the help of that visuals driver will able to take proper decision at right time.<br>
This module will work on IP WebCam by default. You can find the setup of IP WebCam is <a href="https://mishraabhi8924.medium.com/access-the-android-camera-to-python-using-opencv-3d5901f01f23">Here</a>.
This module will also work with system camera. To access the system camera use below code block:- <br>

    import cv2 <br>
    thres = 0.45 # Threshold to detect object<br>
    cap = cv2.VideoCapture(1) #fill the index of your system camera, it is either 0,1 or 2<br>
    cap.set(3,1280)<br>
    cap.set(4,720)<br>
    cap.set(10,70)<br>
    classNames= []<br>
    classFile = 'coco.names'<br>
    with open(classFile,'rt') as f:<br>
    classNames = f.read().rstrip('n').split('n')<br>
    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'<br>
    weightsPath = 'frozen_inference_graph.pb'<br>
    net = cv2.dnn_DetectionModel(weightsPath,configPath)<br>
    net.setInputSize(320,320)<br>
    net.setInputScale(1.0/ 127.5)<br>
    net.setInputMean((127.5, 127.5, 127.5))<br>
    net.setInputSwapRB(True)<br>
    while True:<br>
      success,img = cap.read()<br>
      classIds, confs, bbox = net.detect(img,confThreshold=thres)<br>
      print(classIds,bbox)<br>
      if len(classIds) != 0:<br>
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):<br>
          cv2.rectangle(img,box,color=(0,255,0),thickness=2)<br>
          cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
          cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)<br>
          cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
          cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)<br>
      cv2.imshow('Output',img)<br>
      k=cv2.waitKey(1)<br>
      if k:<br>
        break<br>
    cv2.destroyAllWindows()<br>
    #release the frame<br>
    cap.release()<br>
## Output Screenshot
<img src="../templet/object1.jpeg" alt="Object-detction-output-1"/><br>
<img src="../templet/object2.jpeg" alt="Object-detction-output-2"/>

## How to run the script 
You can run this script by using cmd command, that is:<br>
   `python objectdetection-final.py`
   
For tracking the script follow <a href="https://mishraabhi8924.medium.com/how-to-track-our-python-script-files-f56fe1228d3f">This</a>:point_left: link
