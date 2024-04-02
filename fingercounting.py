import cv2
import time
import os

wCam,hCam=640,480
ptime=0

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    success,img=cap.read()
    # ctime=time.time()
    # fps=1/(ctime-ptime)
    # ptime=ctime
    # print(fps)
    # cv2.putText(img,f'FPS:{str(int(fps))}',(20,100),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
