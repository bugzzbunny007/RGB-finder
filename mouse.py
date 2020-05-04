import cv2
import numpy as np

def click_events(event,x,y,flags,param):
    if event== cv2.EVENT_FLAG_LBUTTON:
        print(x,", ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ' ,' + str(y)
        cv2.putText(img,strxy,(x,y),font,.5,(255,255,0),2)
        cv2.imshow("image",img)
    if event == cv2.EVENT_FLAG_RBUTTON:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue)+' ,'+str(green)+' ,'+str(red)
        cv2.putText(img,strBGR,(x,y),font,.5,(0,255,255),2)
        cv2.imshow('image',img)




img=cv2.imread('lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_events)
cv2.waitKey(0)