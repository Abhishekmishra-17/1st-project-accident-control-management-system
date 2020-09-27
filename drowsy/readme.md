## Applications
This can be used by riders who tend to drive for a longer period of time that may lead to accidents


### Code Requirements
The example code is in Python ([version 3.6](https://www.python.org/download/releases/3.6/) or higher will work). 

### Dependencies

1) import cv2
2) import imutils
3) import dlib
4) import scipy
5) import numpy
6) import urllib

### Description

A computer vision system that can automatically detect driver drowsiness in a real-time video stream and then play an alarm if the driver appears to be drowsy.
This algorithm will work on anroid phone camera(PI webcam).

### Algorithm

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye:.

#### For shape_predictor_68_face_landmarks file:
 Download [shape_predictor_68_face_landmarks](https://drive.google.com/file/d/1O3GdaqCwtGlq5BeUy4DF7z7Cks5J9JNT/view?usp=sharing) file from given link.


*You can use <b>playsound</b> library and create a function that plays the audio file <b>playsound.playsound(path)</b>. Now, after this line, if flag >= frame_check: you can start a thread to play an alarm sound in the background (if the eyes were closed for a sufficient threshold number).*
