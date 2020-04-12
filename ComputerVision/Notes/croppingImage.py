import cv2
import numpy as np
import time as t
path = 'file.png'
img = cv2.imread(path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

draw = False
x1=0
y1=0
x2=0
y2=0
def select(event, x, y, flag, param):
    global draw, x1, y1, x2, y2, img
    if (event==cv2.EVENT_LBUTTONDOWN):
        x1 = x
        y1 = y
        draw = True
        
    elif (event==cv2.EVENT_MOUSEMOVE) and (draw):
        img = cv2.imread(path)
        cv2.rectangle(img,pt1=(x1, y1), pt2=(x, y), color=(0,1,0), thickness=1)
        
    elif (event==cv2.EVENT_LBUTTONUP):
        draw = False
        x2 = x
        y2 = y
        cv2.rectangle(img,pt1=(x1, y1), pt2=(x2, y2), color=(0,1,0), thickness=1)
        crop()
        
def crop():
#         y is height which is actually row and x is width which is actually columns
    print((x1, y1), (x2, y2))
    print('------------------------')
    if y1>y2 and x1>x2:
        selectedImg = img[y2:y1, x2:x1]
    elif y1>y2 and x1<x2:
        selectedImg = img[y2:y1, x1:x2]
    elif y1<y2 and x1>x2:
        selectedImg = img[y1:y2, x2:x1]
    elif y1<y2 and x1<x2:
        selectedImg = img[y1:y2, x1:x2]
    try:
        cv2.imshow('output', selectedImg)
    except:
        pass
    
cv2.namedWindow(winname='image')
cv2.setMouseCallback('image', select)

while True:
    cv2.imshow('image', img)

    if (cv2.waitKey(1) & 0xFF) == -1:
        break

cv2.destroyAllWindows()
t.sleep(3000)