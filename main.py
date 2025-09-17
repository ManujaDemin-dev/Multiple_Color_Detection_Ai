import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while(1):

    _,imageFrame = webcam.read()
    #throwawat variable for bool value :)

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87 , 111], np.uint8)
    red_upper = np.array([180, 255 , 255], np.uint8)
    red_mask =cv2.inRange(hsvFrame , red_lower , red_upper )


    green_lower = np.array([25, 52 , 72], np.uint8)
    green_upper = np.array([102, 255 , 255], np.uint8)
    green_mask =cv2.inRange(hsvFrame , green_lower , green_upper)    

    blue_lower = np.array([94, 80 , 2], np.uint8)
    blue_upper = np.array([120, 255 , 255], np.uint8)
    blue_mask =cv2.inRange(hsvFrame , blue_lower , blue_upper)





