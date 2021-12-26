#!/usr/bin/env python3
#-*- condinf: utf-8 -*-

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("origin",cv2.WINDOW_NORMAL)

cv2.createTrackbar("H_l", "origin", 0, 180, nothing)
cv2.createTrackbar("H_h", "origin", 0, 180, nothing)
cv2.createTrackbar("S_l", "origin", 0, 255, nothing)
cv2.createTrackbar("S_h", "origin", 0, 255, nothing)
cv2.createTrackbar("V_l", "origin", 0, 255, nothing)
cv2.createTrackbar("V_h", "origin", 0, 255, nothing)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while(1):
    ret,img = cap.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_l = cv2.getTrackbarPos("H_l", "origin")
    h_h = cv2.getTrackbarPos("H_h", "origin")
    s_l = cv2.getTrackbarPos("S_l", "origin")
    s_h = cv2.getTrackbarPos("S_h", "origin")
    v_l = cv2.getTrackbarPos("V_l", "origin")
    v_h = cv2.getTrackbarPos("V_h", "origin")
 
    lower = np.array([h_l, s_l, v_l])
    upper = np.array([h_h, s_h, v_h])
    img_mask_blue = cv2.inRange(hsv, lower, upper)
    img_color_blue = cv2.bitwise_and(img ,img, mask=img_mask_blue)
    cv2.imshow("origin",img)
    cv2.imshow("mask", img_color_blue)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        lower = [h_l, s_l, v_l]
        upper = [h_h, s_h, v_h]
        print(lower)
        print(upper)
        break
                
cap.release()
cv2.destroyAllWindows()
