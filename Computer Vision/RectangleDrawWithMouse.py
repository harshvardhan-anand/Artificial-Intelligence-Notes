import cv2 
import numpy as np

# function to draw
count = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
def draw(event, x, y, flags, param):
    global count, x1, y1, x2, y2
    if (event == cv2.EVENT_LBUTTONDOWN) and count == 0:
        x1 = x
        y1 = y
        count+=1
    elif (event == cv2.EVENT_LBUTTONDOWN) and count == 1:
        x2 = x
        y2 = y
        count = 0
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(0,3,0), thickness=1)
#     else:
#         cv2.rectangle(img , pt1=(0,500), pt2=(500, 0), color=(0,0,0), thickness=-1)
        
# connect to Callback function to draw
cv2.namedWindow(winname = "Title_bar")
cv2.setMouseCallback('Title_bar', draw)

# image to show

img = np.zeros([500, 500, 3])

# window operation


# if we use "and" instead of "&" then the operation will not work because here we are doing bitwise and between "cv2.waitKey(1)"and
# binary of 0xFF and checking whether the value of "(cv2.waitKey(1) & 0xFF)" is equal to ordinal value of q or say numeric value of "q"

# https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
# https://stackoverflow.com/questions/53357877/usage-of-ordq-and-0xff?rq=1

while True:
    cv2.imshow('Title_bar', img)
    
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
        
cv2.destroyAllWindows()