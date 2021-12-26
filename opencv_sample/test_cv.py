import cv2
import numpy as np

def masking(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv_min = np.array([160, 100, 100])
    hsv_max = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)





def filter(img):
    kernel = np.ones((5,5), np.float32) / 5
    dst = cv2.filter2D(img, -1, kernel)

    return dst

def main():
    img = cv2.imread('ball_kyougidai.png')

    while(1):
        img = kernel(img)
        mask = masking(img)

        



