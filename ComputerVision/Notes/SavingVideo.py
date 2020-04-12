import cv2

cap = cv2.VideoCapture(0)

# Writer

# cv2.VideoWriter( filename, fourcc, fps, frameSize )

# filename	Name of the output video file.
# fourcc	video codec differnt for linux, mac and windows
# fps	Framerate of the created video stream.
# frameSize	Size of the video frames.
# isColor	If it is not zero, the encoder will expect and encode color frames, otherwise it will work with grayscale frames 
#         (the flag is currently supported on Windows only).

# higher the fps higher is the file size. High fps means high is the quality of video i.e more details are captured
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('firstrecording.avi', codec, 20, (width, height))
# DIVX encodes for .avi file type

# in while loop show video until break
while True:
    ret, frame = cap.read()
    
    #writing
    writer.write(frame)
    
    cv2.imshow('Video', frame)
    if (cv2.waitKey(1)&0xFF)==27:
        break

# release recoder, writer, destroyAll
cap.release()
writer.release()
cv2.destroyAllWindows()