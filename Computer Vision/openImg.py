import cv2
import matplotlib.pyplot as plt


img = cv2.imread('image.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('flower', img)
cv2.waitKey()

cv2.destroyAllWindows()