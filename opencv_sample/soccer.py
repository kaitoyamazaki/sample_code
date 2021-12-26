import cv2
import numpy as np
import os


def white_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_hsv = np.array([0, 0, 100])
    upper_hsv =np.array([180,45,255])
    mask = cv2.inRange(hsv, low_hsv, upper_hsv)

    return mask


def kernel(img):
    kernel = np.ones((5,5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)

    return dst

def main():

    cap = cv2.VideoCapture('soccer.mp4')
    cap.set(3, 1280)
    cap.set(4, 720)

    while(cap.isOpened()):
        ret, frame = cap.read()

        frame = kernel(frame)
        mask = white_mask(frame)

        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

    
