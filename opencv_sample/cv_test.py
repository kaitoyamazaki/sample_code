import cv2
import numpy as np


def red_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_hsv = np.array([160, 100, 100])
    upper_hsv = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, low_hsv, upper_hsv)

    return mask1

    
def analysis_pic(mask):
    #2値画像のラベリング処理
    label = cv2.connectedComponentsWithStats(mask)

    # ブロブ情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)

    max_index = np.argmax(data[:, 4])
    maxblob = {}

    maxblob["upper_left"] = (data[:, 0][max_index], data[:, 1][max_index]) # 左上座標
    maxblob["width"] = data[:, 2][max_index]  # 幅
    maxblob["height"] = data[:, 3][max_index]  # 高さ
    maxblob["area"] = data[:, 4][max_index]   # 面積
    maxblob["center"] = center[max_index]  # 中心座標

    return maxblob

def kernel(img):
    kernel = np.ones((5,5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)

    return dst


def main():
        
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    while(cap.isOpened()):
        ret, frame = cap.read()

        frame = kernel(frame)
        mask = red_mask(frame)

        target = analysis_pic(mask)

        center_x = int(target["center"][0])
        center_y = int(target["center"][1])
            
        cv2.circle(frame, (center_x, center_y), 75, (0, 200, 0), thickness=3, lineType=cv2.LINE_AA)

        # 結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
            
        # qキーが押されたら途中終了
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
