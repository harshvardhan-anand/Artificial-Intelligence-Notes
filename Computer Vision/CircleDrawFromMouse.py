import cv2
import numpy as np

# function to draw
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=100, color=(0,255,0), thickness=1)
    
#connecting to callback function
cv2.namedWindow(winname='Image')
cv2.setMouseCallback('Image', draw)

# Image to show and quit the window
img = np.zeros([500, 500, 3], np.uint8)
while True:
    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()

