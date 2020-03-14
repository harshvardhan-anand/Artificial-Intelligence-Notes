import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('firstrecording.avi', codec, 20, (width, height))

cap.release()
writer.release()
cv2.destroyAllWindows()