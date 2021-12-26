#!/usr/bin/python3

import cv2

cap = cv2.VideoCapture(2)
cap.set(3, 1280)
cap.set(4, 720)

try:
    while(True):
        ret, frame = cap.read()

        if ret == False:
            print("no camera")
            break
        else:
            cv2.imshow('cam_capture0',frame)
            k = cv2.waitKey(1)
            if k == 27:
                break
except KeyboardInterrupt:
    print("Ctl+C")

cap.release()
cv2.destroyAllWindows()

#original author -- Koki Shirota
