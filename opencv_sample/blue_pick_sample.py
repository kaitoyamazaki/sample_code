#original author -- Koki Shirota

import cv2
import numpy as np

cap = cv2.VideoCapture(0) ##カメラから映像を取得
cap.set(3, 1280)
cap.set(4, 720)

while(1):
    ret, frame = cap.read() #取得したカメラデータの読み込み
    kernel = np.ones((5,5), np.float32)/ 25
    frame = cv2.filter2D(frame, -1, kernel)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)# BGRからhsvに空間を変換

    #青色の変換
    lower_blue = np.array([160, 100, 100])
    upper_blue = np.array([180, 255, 255])
    img_mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    img_color_blue = cv2.bitwise_and(frame, frame, mask=img_mask_blue)

    cv2.imshow("SHOW COLOR DEFAULT", frame) 
    cv2.imshow("SHOW COLOR BLUE", img_mask_blue)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


#original author -- Koki Shirota
