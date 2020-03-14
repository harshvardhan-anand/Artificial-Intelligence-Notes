import cv2
import numpy as np

# function to draw
x1, y1, running=0, 0, 0
def draw(event , x, y, flags, param):
    global x1, y1, running
    if (event == cv2.EVENT_LBUTTONDOWN) and (running == 0):
        x1, y1, running = x, y, 1
        print("Operation : LBUTTONDOWN at", x1, y1 , "and running :", running)  #log
        
    if (event == cv2.EVENT_MOUSEMOVE) and (running is 1):
        x2 = x
        y2 = y
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x, y), color=(12,12,0), thickness=-1)
        print("Operation : DRAWING, LBUTTONDOWN at", x, y , "and running :", running)  #log

    elif (event == cv2.EVENT_LBUTTONUP) and (running is 1):
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x, y), color=(12,12,0), thickness=-1)
        running = 0
        print("Operation : End drawing at", x, y , "and running :", running)  #log
        
    if (event == cv2.EVENT_RBUTTONDOWN) :
        #log
        print("------------------------------------------------------------------------------------------")
        
# connection to Callback function
print('connecting to callback function')
cv2.namedWindow(winname="titlebox")
cv2.setMouseCallback("titlebox", draw)
print('passed connection to callback function')

# image on which we have to draw
print("Creating image")
img = np.zeros((500, 500, 3))
print("Created image")

# operation to windows
while True:
    #print("Inside while loop and showing image")
    cv2.imshow("titlebox", img)
    #print("waiting to disconnect")
    if (cv2.waitKey(1)&0xFF)==27:
        print("Disconnected")
        break
# print(cv2.waitKey(1))
print("Destroying all windows")
cv2.destroyAllWindows()
    