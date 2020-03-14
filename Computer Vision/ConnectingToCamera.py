import cv2


# if access to the camera is denied by the system then we will get error saying src is empty " error: (-215:Assertion failed)!_src.empty() in function 'cv::cvtColor'"
# so allow access to chrome or brwser you are using to run the .py file of .ipynb file to use camera. You can also find this error if you have antivirus blocking use of camera.So stop it also.

capture = cv2.VideoCapture(0) # "0" means use default camera
                              # "1" means use camera connected to port

width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    
#     ret is true if capturing
    ret, frame = capture.read()
    
#     grayscalevideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to balck and white
    cv2.imshow('frame', frame)
    
    if (cv2.waitKey(1)& 0xFF) == 27:
        break
        
capture.release()  #release camera i.e do not use camera
cv2.destroyAllWindows()