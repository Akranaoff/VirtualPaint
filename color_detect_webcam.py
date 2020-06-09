import cv2
import numpy as np

frameWidth = 440
frameHeight = 280
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,200)

def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("Hue minimum","TrackBars",0,179,empty)
cv2.createTrackbar("Satu minimum","TrackBars",0,255,empty)
cv2.createTrackbar("Val minimum","TrackBars",0,255,empty)
cv2.createTrackbar("Hue maximum","TrackBars",179,179,empty)
cv2.createTrackbar("Satu maximum","TrackBars",255,255,empty)
cv2.createTrackbar("Val maximum","TrackBars",255,255,empty)

while True:
    _, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue minimum","TrackBars")
    s_min = cv2.getTrackbarPos("Satu minimum", "TrackBars")
    v_min = cv2.getTrackbarPos("Val minimum", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue maximum", "TrackBars")
    s_max = cv2.getTrackbarPos("Satu maximum", "TrackBars")
    v_max = cv2.getTrackbarPos("Val maximum", "TrackBars")

    print(h_min)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,imgResult])



    cv2.imshow("Horizontal Stack", hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()