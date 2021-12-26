import cv2
import numpy as np



def main():
        
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)


    while(1):
        ret,frame = cap.read()
        #image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow('BGR Color', frame)
        cv2.imshow('hsv_image', hsv_image)


        k = cv2.waitKey(1)
        if k == 27:
            break


    cv2,release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
